# Welcome to "notgoogle.com" : The Smallest Search Engine
This is search engine built using Vector Space Model on the <strong>Cornell Movie-Dialogs Corpus</strong>.


## Setup, Installation and Usage
- Make sure you have `pip` and `virtualenv` installed on your systems (Examples given for ubuntu)
	- `sudo apt install python3-pip` : To install pip
	- `pip3 install virtualenv` : To install virtualenv
- Execute the following commands from the root of the project to setup the project:
	- `virtualenv env` : Create python virutal environment for the project
	- `source env/bin/activate` : Activate the virtual environment for the project
	- `pip install -r requirements.txt` : Install the required dependencies for the project
	- Install the nltk dependencies: (Run python in the shell and then run the following)
		``` 
		import nltk
		nltk.download('putnk')
		nltk.download('stopwords')
		nltk.download('wordnet')
		```
	- `python setup.py` : Finish setting up the necessary requirements for the project like the inverted index.
	- `python app.py` : Run the application (`Ctrl + C` : Stop the flask server)
	- `deactivate` : To deactivate the virtual environment (Do not deactivate the environemnt during any of the above steps)

## Folder Strucuture
```
.
├── app.py
├── docs
│   ├── app.html
│   └── src
│       ├── index.html
│       ├── search.html
│       ├── tf_idf_indexer.html
│       └── utilities.html
├── README.md
├── requirements.txt
├── setup.py
└── src
   ├── datasets
   │   ├── cornell movie-dialogs corpus
   │   │   ├── movie_characters_metadata.txt
   │   │   ├── movie_conversations.txt
   │   │   ├── movie_lines.txt
   │   │   ├── movie_titles_metadata.txt
   │   │   ├── raw_script_urls.txt
   │   │   └── README.txt
   │   └── pickle_files
   │       ├── inverted_index.pickle
   │       └── movies_metadata.pickle
   ├── search.py
   ├── site
   │   ├── index.html
   │   └── results.html
   ├── tf_idf_indexer.py
   └── utilities.py


```