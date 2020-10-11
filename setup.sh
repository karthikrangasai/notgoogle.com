echo -e "\e[1m>>> Running checks for roe.com"
echo -e "\e[0m"

# Check for virtualenv
echo -ne "\e[1m>> Checking if 'virtualenv' is present: "
venv_bool=$(pip3 freeze | grep virtualenv)

if [[ $venv_bool == "" ]]
then
	echo -e "\e[0mNo.\nStarting Download"
	pip3 install virtualenv
else
	echo -e "\e[0mYes."
fi

# Check for dataset
# echo -ne "\e[1m>> Checking if dataset is present: "
# DATASET=./Cell_Phones_and_Accessories_5.json.gz
# if [[ -f "$DATASET" ]]
# then
# 	echo -e "\e[0mYes."
# else
# 	echo -e "\e[0mNo.\nStarting Download"
# 	wget http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Cell_Phones_and_Accessories_5.json.gz
# fi

# Check for virtual environment
echo -ne "\e[1m>> Checking if virtual environment is present: "
if [[ -d "./env" ]]
then
        echo -e "\e[0mYes."
else
        echo -e "\e[0mNo.\nCreating Virtual Environemt"
        virtualenv env
fi

source "env/bin/activate"

pip install -r requirements.txt
mkdir env/lib/nltk_data
python -c "import nltk ; nltk.download('putnk', download_dir=os.path.join(os.getcwd(), \"env/lib/nltk_data\"))"
# pip freeze > requirements.txt