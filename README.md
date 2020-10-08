# Welcome to notgoogle.com : The Smallest Search Engine

## Setup, Installation and Usage
- If you have cloned the project for the first time, run the `setup.sh` file first. This file checks and installs virtualenv, creates a virtual environment and downloads the dataset.
- Enter the virtual environment using `source env/bin/activate` and use `deactivate` to exit the environemnt
- Run the command `pip freeze > requirements.txt` to save the latest addition of pytohn ackages you have installed.

## Explanation

## To-Dos
- Write bash script to generate inital lyrics dataset ( Kathik )
- Write bash scripts `run.sh` and `test.sh` ( Karthik )
- Program the TF-IDF indexer ( Gaurav )
- Program the Flask App for presentation ( Karthik, Shanmukh )

## Folder Strucuture
```
.
├── datasets
├── env
├── src
├── README.md
├── requirements.txt
├── run.sh
├── setup.sh
├── test.sh
├── app.py
└── test.py
```
- `datasets` and `env` are generated when running `setup.sh`
- All the python code for the project will be present in `src`
- `run.sh` is the bash script to run the python program (search engine)
- `app.py` will be the main Python file to run the program, called in `run.sh`
- `test.py` will be the testing file for the Python program, called in `test.sh`