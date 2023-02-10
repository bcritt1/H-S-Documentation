import gensim

"""The syntax of the next statement is as follows:

model =: Assigning our model to the variable "model" via Python syntax.
gensim.models.Word2Vec: Calling the gensim function Word2Vec to tell it which word embedding algorithm to use. Others include FastText, Doc2Vec, and Stanford's GLoVe.
sentences: Telling the function what dataset to run on. Remember "sentences" is a sentence tokenized Python list of our corpus.
min_count: An option telling gensim the minimum times a word should occur in the corpus to be incorporated in the model. We want it to include all words so we set this to 0. If you have a concern that unique words will skew your model, you can set this higher to include only words that appear more frequently.
vector_size=100: The number of coordinates gensim will use to describe each word vector. The model will be more accurate the higher this number is, but it will also take more time to compute.
sg=1: Sets the method for the embedding. 1 is skip-gram, 0 is CBOW. Skip-gram is thought to be more accurate on smaller corpora, so we will use that."""

#Create model according to paramaters above. "sentences" is the output of the tokenizer.py script, reimported from json as below:

#Reimport with:
#with open("data.json", "r") as read_file:
#    data = json.load(read_file)
model = gensim.models.Word2Vec(sentences, min_count=0, vector_size=100, sg = 1)

#Save the model locally so we don't need to retrain it every time we open our notebook. 
model.save('my_model')

#If you save your model, in the future you can start at this line, loading in the model from disk. 
my_model = gensim.models.Word2Vec.load('my_model') 