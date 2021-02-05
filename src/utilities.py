from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer

# Total number of documents
NUMBER_OF_DOCUMENTS = 617

# File encoding used in the dataset
FILE_ENCODING = "ISO-8859-1"

# A dictionary of the dataset files.
DATATSET = {
	'movie_lines' : 'movie_lines.txt',
	'movie_conversations' : 'movie_conversations.txt',
	'movie_char_metadata' : 'movie_characters_metadata.txt',
	'movie_titles_metadata' : 'movie_titles_metadata.txt'

}

# A dictionary of the pickle files used for storing the model and the movies' metadata
MODELS = {
	'movies' : 'movies_metadata.pickle',
	'inverted_index' : 'inverted_index.pickle'
}

tokenizer = RegexpTokenizer("[\w']+")
porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
stopwords_set = set(stopwords.words('english'))

def preprocess_lines(movie_line):
	"""
	Given a movie line , generate terms, stem the terms and generate tokens.

	Args:
		movie_line (str): The string to be processed before indexing it.

	Returns:
		list: A list of processed tokens.
	"""
	tokens = tokenizer.tokenize(movie_line)
	words = [word for word in tokens if word not in stopwords_set]
	stemmed_terms = [porter_stemmer.stem(word) for word in words]
	lemmatized_terms = [wordnet_lemmatizer.lemmatize(word) for word in stemmed_terms]
	return lemmatized_terms