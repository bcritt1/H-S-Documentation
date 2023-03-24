# Import additional "mathy" libraries for data manipulation and PCA

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

#import visualization library

%matplotlib inline
import matplotlib.pyplot as plt
import plotly.graph_objects as go

#If you saved your model from "embedding.py", import with:

my_model = gensim.models.Word2Vec.load('my_model') 

#Create 2d df
vocab = list(my_model.wv.key_to_index)
X = my_model.wv[vocab]

pca = PCA(n_components=2)
result = pca.fit_transform(X)

pca_df = pd.DataFrame(result, columns = ['x', 'y'])
pca_df['word'] = vocab

#Create 3d df
pca3d = PCA(n_components=3)
result3d = pca3d.fit_transform(X)

pca_df3d = pd.DataFrame(result3d, columns = ['x', 'y', 'z'])
pca_df3d['word'] = vocab


####HOW TO ADAPT TO HPC? XEYES?
#2d graph
N = 1000000
words = vocab
fig = go.Figure(data=go.Scattergl(
   x = pca_df['x'],
   y = pca_df['y'],
   mode='markers',
   marker=dict(
       color=np.random.randn(N),
       colorscale='Viridis',
       line_width=1
   ),
   text=pca_df['word'],
   textposition="bottom center"
))

fig.show()

#3d graph
N = 1000000
words = vocab
fig = go.Figure(data=go.Scatter3d(
   x = pca_df3d['x'],
   y = pca_df3d['y'],
    z= pca_df3d['z'],
   mode='markers',
   marker=dict(
       color=np.random.randn(N),
       colorscale='Viridis',
       line_width=1
   ),
   text=pca_df3d['word'],
   textposition="bottom center"
))

fig.show()

#Built-in gensim functions to explore model mathematically

#syntactic similarity of 2 words, measured by cosine similarity (comparitive angle of vectors)
my_model.wv.similarity('aristotle','bacon')

# 10 most similar words to w words
my_model.wv.most_similar('aristotle'), my_model.wv.most_similar('bacon')

# n most similar words to word x
my_model.wv.most_similar('aristotle', topn=20)

#create a list of candidates and ask gensim which is the most similar in the word space.

candidates = ['city','spirit','god','soul']
model.wv.most_similar_to_given('nature', candidates)

#see their similarity scores

for c in candidates:
    print(c, my_model.wv.similarity('nature',c))

# List words closer than 2 given words
model.wv.closer_than('nature','soul') #also try "soul"