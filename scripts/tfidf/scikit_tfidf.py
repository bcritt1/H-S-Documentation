#Adapted from https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf
import os
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

user = os.getenv('USER')
#corpusdir = '/scratch/users/{}/corpus/'.format(user)
all_txt_files =[]
for file in Path("/scratch/users/{}/corpus/".format(user)).rglob("*.txt"):
     all_txt_files.append(file.parent / file.name)
# counts the length of the list
n_files = len(all_txt_files)
print(n_files)

all_docs = []
for txt_file in all_txt_files:
    with open(txt_file) as f:
        txt_file_as_string = f.read()  
    all_docs.append(txt_file_as_string)

vectorizer = TfidfVectorizer(max_df=.65, min_df=1, stop_words=None, use_idf=True, norm=None)
transformed_documents = vectorizer.fit_transform(all_docs)

transformed_documents_as_array = transformed_documents.toarray()

# make the output folder if it doesn't already exist
Path("/scratch/users/{}/outputs/tf_idf_output".format(user)).mkdir(parents=True, exist_ok=True)

# construct a list of output file paths using the previous list of text files the relative path for tf_idf_output
output_filenames = [str(txt_file).replace(".txt", ".csv").replace("/scratch/users/{}/corpus/".format(user),
"/scratch/users/{}/outputs/tf_idf_output/".format(user)) for txt_file in all_txt_files]

# loop each item in transformed_documents_as_array, using enumerate to keep track of the current position
for counter, doc in enumerate(transformed_documents_as_array):
    # construct a dataframe
    tf_idf_tuples = list(zip(vectorizer.get_feature_names_out(), doc))
    one_doc_as_df = pd.DataFrame.from_records(tf_idf_tuples, columns=['term', 'score']).sort_values(by='score', ascending=False).reset_index(drop=True)
    
    # output to a csv using the enumerated value for the filename
    one_doc_as_df.to_csv(output_filenames[counter])

