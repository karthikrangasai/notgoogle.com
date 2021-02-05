# Check the for the necessary files - The dataset i.e. documents for showing in the webpages, the virtual environment and the tf-idf index matrix
# If all checks pass, run the flask app, else throw an error



source env/bin/activate

echo "[INFO] Starting the tf_idf indexer to generate inverted index."
python src/tf_idf_indexer.py
echo "[INFO] Running the Flask Application"
python app.py

deactivate