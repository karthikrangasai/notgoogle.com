import math
import pickle
import os
import time
from .utilities import NUMBER_OF_DOCUMENTS, FILE_ENCODING, DATATSET, MODELS, preprocess_lines
from autocorrect import Speller

auto_spell = Speller()
query_vector = {} # The dictionary object that stores the frequency of each term, from the query, in the query


# Loading the file that contains the metadata for the movies
with open(os.path.join(os.getcwd(), "src/datasets/pickle_files/" + MODELS['movies']), 'rb') as movies_file:
    movies = pickle.load(movies_file)

# Loading the file that contains the inverted index for the search engine
with open(os.path.join(os.getcwd(), "src/datasets/pickle_files/" + MODELS['inverted_index']), 'rb') as index_file:
    inverted_index = pickle.load(index_file)


def __term_frequency(term, document, query=False):
	"""
	Computes the raw term frequency of a term in the document.

	Args:
		term (str): The term whose frequency is to be computed.
		document (str): Document ID as present in the inverted_index dictionary.
	    query (bool): If True, computes the term frequency of the term in the query, else in the document
        (default is False)

	Returns:
		An integer
	"""
	if query:
		return query_vector[term]
	if document not in inverted_index[term].keys():
		return 0
	return inverted_index[term][document]

def __log_term_frequency(term, document, query=False):
	"""
	Computes the logartihmic term frequency of a term in the document.

	Args:
		term (str): The term whose frequency is to be computed.
		document (str): Document ID as present in the inverted_index dictionary.
	    query (bool): If True, computes the term frequency of the term in the query, else in the document
        (default is False)

	Returns:
		An floating point value
	"""
	if __term_frequency(term, document, query) > 0:
		return 1 + math.log(__term_frequency(term, document, query))
	return 0

def __augmented_term_frequency(term, document, query=False):
	"""
	Computes the augmented term frequency of a term in the document.

	Args:
		term (str): The term whose frequency is to be computed.
		document (str): Document ID as present in the inverted_index dictionary.
	    query (bool): If True, computes the term frequency of the term in the query, else in the document
        (default is False)

	Returns:
		An floating point value
	"""
	max_term_frequency = -1
	for t in inverted_index.keys():
		max_term_frequency = max(max_term_frequency, __term_frequency(t, document, query))
	return 0.5 + 0.5 * ( __term_frequency(term, document, query) / max_term_frequency )

def __boolean_term_frequency(term, document, query=False):
	"""
	Computes the boolean term frequency of a term in the document.

	Args:
		term (str): The term whose frequency is to be computed.
		document (str): Document ID as present in the inverted_index dictionary.
	    query (bool): If True, computes the term frequency of the term in the query, else in the document
        (default is False)

	Returns:
		Either 0 or 1
	"""
	if __term_frequency(term, document, query) > 0:
		return 1
	return 0

def __document_frequency(term):
	"""
	Computes the raw document frequency of a term.

	Args:
		term (str): The term whose document frequency is to be computed.

	Returns:
		An integer
	"""
	return len(inverted_index[term])

def __inverted_documnent_frequency(term):
	"""
	Computes the inverted document frequency of a term.

	Args:
		term (str): The term whose document frequency is to be computed.

	Returns:
		An floating point value
	"""
	return math.log(movies['num_of_movies'] / __document_frequency(term))


def __score(term, document, scoring_scheme, query):
	"""
	Computes the tf-idf score of a term from the query in the document/qeury.

	Args:
		term (str): The term whose tf-idf score is to be computed.
		document (str): The document for which the tf-idf score is to be computed.
		scoring_scheme (char) : A character denoting the type of scoring scheme to be used.
	    query (bool): If True, computes the tf-idf score of the term in the query, else in the document
        (default is False)


	Returns:
		An floating point value
	"""
	term_frequency_type = scoring_scheme
	if term_frequency_type ==  "n":
		term_frequency = __term_frequency(term, document, query)
	elif term_frequency_type == "l":
		term_frequency = __log_term_frequency(term, document, query)
	elif term_frequency_type == "a":
		term_frequency = __augmented_term_frequency(term, document, query)
	elif term_frequency_type == "b":
		term_frequency = __boolean_term_frequency(term, document, query)

	return term_frequency * __inverted_documnent_frequency(term)

def search(query, scoring_scheme):
	"""
	Searches for a given query in a set of documents.

	Args:
		query (str): The string to be matched in documents.
		scoring_scheme (char) : A character denoting the type of scoring scheme to be used for the matching.

	Returns:
		list: A list of the top 10 matched documents.
	"""
	correct_query = auto_spell(query)
	print("Query: ", query, " and Corrected Query: ", correct_query)
	query_is_misspelt = (query != correct_query)
	# if query_is_misspelt:
	# 	query = correct_query

	# query_vector = [ tf_1,q , tf_2,q, ..., tf_n,q]

	# scores = [
	# 	[score-1, doc-1] # [float, int]
	# 	[score-2, doc-2]
	# 	.
	# 	.
	# 	[score-n, doc-n]
	# ]

	# inverted_index : {
	# 	term-1 : [ {doc_i, tf_t_doci} , {}, ]
	# 	term-2 : [ {doc_i, tf_t_doci} , {}, ]
	# 	.
	# 	.
	# 	term-2 : [ {doc_i, tf_t_doci} , {}, ]
	# }

	global query_vector
	query_vector = {}
	scores = [[0.0, i] for i in range(0,NUMBER_OF_DOCUMENTS)]
	length = [0.0] * movies['num_of_movies']
	start = time.time()
	query_terms = preprocess_lines(query)
	end = time.time()
	print("[INFO] Preprocessing Query Time : ", (end - start), " seconds")

	start = time.time()
	for term in inverted_index.keys():
		if term in set(query_terms):
			if term in query_vector.keys():
				query_vector[term] += 1
			else:
				query_vector[term] = 1
		else:
			query_vector[term] = 0
	
	query_length = 0.0
	for term in query_terms:
		if term not in inverted_index.keys():
			continue
		weight_of_term_in_query = __score(term, None, scoring_scheme, True)
		for document in inverted_index[term]:
			id = int(document[1:])
			scores[id][0] += weight_of_term_in_query * __score(term, document, scoring_scheme, False)
			# length[id] += 1
			if inverted_index[term][document] > 0:
				length[id] += 1

	for d in range(0, NUMBER_OF_DOCUMENTS):
		if length[d] > 0:
			scores[d][0] = scores[d][0] / length[d]

	scores.sort(key = lambda x: x[0], reverse=True)
	scores = scores[:10]
	end = time.time()
	print("[INFO] Retrieving Documents Time : ", (end - start), " seconds")
	
	ans = {} # Holds the final result of the top 10 documents
	
	if scores[0][0] == 0.0:
		ans['query_error'] = "No Documents match the query. Please check the query."
	else:
		ans['query_error'] = ""

	if query_is_misspelt:
		ans['correct_query'] = "Did you mean: \"" + correct_query + "\""
	else:
		ans['correct_query'] = ""
	
	ans['movies'] = {}
	for score in scores:
		m = {}
		m['score'] = score[0]
		m['name'] = movies["m" + str(score[1])]['name'].upper()
		m['year'] = movies["m" + str(score[1])]['year']
		m['rating'] = movies["m" + str(score[1])]['rating']
		ans['movies']["m" + str(score[1])] = m
	
	return ans







