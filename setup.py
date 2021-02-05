import os
import nltk
from src import tf_idf_indexer

print("\t\t\t\t CS F469 - INFORMATION RETREIVAL")
print("\t\t\t\t\t Assignment I")
print("\n")
print(">>>>>> SETUP: \n\n")

print("\n\n>> Running the Inverted Index Generator: \n")
movie_ids = tf_idf_indexer.generate_movie_file_and_return_movie_ids()
movie_dataset = tf_idf_indexer.preprocess_dataset(movie_ids=movie_ids)
tf_idf_indexer.generate_inverted_index(movie_dataset=movie_dataset)