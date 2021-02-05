import pickle
import os
import time
from utilities import FILE_ENCODING, DATATSET, MODELS, preprocess_lines


def generate_movie_file_and_return_movie_ids():
	"""
	Generates the dictionary file of the metadata of the movies.

	Returns:
		list: An list of strings which represent the movie ids.
	"""
	movies = {
		'num_of_movies' : 0
	}
	movie_ids = []

	print("[INFO] Starting Movie Metadata Generation.")

	with open(os.path.join(os.getcwd(), "src/datasets/cornell movie-dialogs corpus/" + DATATSET['movie_titles_metadata']), encoding=FILE_ENCODING) as f:
		line = f.readline()
		while line:
			movie = {}
			movie_metadata_values = line.split(" +++$+++ ")
			if len(movie_metadata_values) == 6:
				movie_ids.append(movie_metadata_values[0])
				movie['name'] = movie_metadata_values[1]
				movie['year'] = movie_metadata_values[2]
				movie['rating'] = movie_metadata_values[3]
				movies[movie_metadata_values[0]] = movie
				movies['num_of_movies'] += 1
			
			line = f.readline()

	print("[INFO] Finished generating Movie Metadata.")

	print("[INFO] Preparing to save the generated movies' metadata.")
	
	file_path = os.path.join(os.getcwd(), "src/datasets/pickle_files/" + MODELS['movies'])
	with open(file_path, mode='w+b') as movies_file:
		pickle.dump(movies, movies_file, protocol=pickle.HIGHEST_PROTOCOL)

	print("[INFO] Saved the generated Movie Metadata file at %s." % (file_path))
	
	return movie_ids

def preprocess_dataset(movie_ids):
	"""
	Preporcesses the entire dataset i.e. remove stop words, stem, and lemmatize the movie dialouges.

	Args:
		movie_ids (list): An list of strings which represent the movie ids.

	Returns:
		dict: A dictionary that maps each movie to a list of all the processed dialouges in that movie. 
	"""
	if not isinstance(movie_ids, list):
		raise AssertionError("movie_ids must be an object of type list.")

	print("[INFO] Starting Data Preprocessing.")
	start = time.time()

	dialouges = {}

	with open(os.path.join(os.getcwd(), "src/datasets/cornell movie-dialogs corpus/" + DATATSET['movie_lines']), encoding=FILE_ENCODING) as f:
		line = f.readline()
		while line:
			terms = []
			dialouge_line_values = line.split(" +++$+++ ")
			if dialouge_line_values[2] not in dialouges.keys():
				dialouges[dialouge_line_values[2]] = dialouge_line_values[4]
				dialouges[dialouge_line_values[2]] += "\n"
			else:
				dialouges[dialouge_line_values[2]] += dialouge_line_values[4]
				dialouges[dialouge_line_values[2]] += "\n"	
			line = f.readline()

	movie_dataset = dict.fromkeys(dialouges.keys(), [])
	for movie_id in dialouges:
		movie_dataset[movie_id] = preprocess_lines(dialouges[movie_id])

	end = time.time()
	print("[INFO] Finished Data Preporcessing.")
	print("[INFO] Time taken to preprocess data is %f seconds" % (end - start))

	
	return movie_dataset



def generate_inverted_index(movie_dataset):
	"""
	Generate the inverted index from the given set of documents

	Args:
		movie_dataset (dict): dict: A dictionary that maps each movie to a list of all the processed dialouges in that movie. 
	"""
	if not isinstance(movie_dataset, dict):
		raise AssertionError("movie_dataset must be an object of type dict.")
	
	print("[INFO] Strating Inverted Index generation.")
	start = time.time()

	inverted_index = {}
	for movie_id in movie_dataset:
		for word in movie_dataset[movie_id]:
			if word not in inverted_index.keys():
				movie = {}
				movie[movie_id] = 1
				inverted_index[word] = movie
			else:
				if movie_id not in inverted_index[word].keys():
					inverted_index[word][movie_id] = 1
				else:
					inverted_index[word][movie_id] += 1
	
	end = time.time()
	print("[INFO] Inverted Index generated.")
	print("[INFO] Time taken to generate inverted index is %f seconds" % (end - start))

	print("[INFO] Preparing to save the generated Inverted Index.")

	file_path = os.path.join(os.getcwd(), "src/datasets/pickle_files/" + MODELS['inverted_index'])
	with open(file_path, mode='w+b') as index_file:
		pickle.dump(inverted_index, index_file, protocol=pickle.HIGHEST_PROTOCOL)
	
	print("[INFO] Saved the generated Inverted Index at %s." % (file_path))