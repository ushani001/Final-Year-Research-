#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from pandas import read_csv

import pandas as pd
df = pd.read_csv("../input/phone-reviews/convertedJson_phone_review.csv")


df.rename(columns={'reviewText':'Text'}, 
                 inplace=True)



fig = plt.figure(figsize=(8,7))
colors=["hotpink","violet","yellow","forestgreen","chartreuse"]
df['overall'].value_counts( sort=False).plot(kind = 'pie', autopct='%1.2f%%',fontsize=10 , startangle=90,colors=colors,counterclock=False)
plt.title('Rating')
plt.legend(labels=['1','2','3','4','5']) #colors --> party name
plt.tight_layout() #regularity
plt.show()

import random
from sklearn.utils import shuffle
combine = [df]
Score_mapping = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}
for dataset in combine:
    dataset['overall'] = dataset['overall'].map(Score_mapping)
    dataset['overall'] = dataset['overall'].fillna(0)

fig = plt.figure(figsize=(8,7))
colors=["coral","yellow","chartreuse"]
df['overall'].value_counts( sort=False).plot(kind = 'pie', autopct='%1.2f%%',fontsize=10 , startangle=90,colors=colors,counterclock=False)
plt.title('Rating')
plt.legend(labels=['1','2','3','4','5']) #colors --> party name
plt.tight_layout() #regularity
plt.show()


rating_1 = df[df['overall'] == 1].iloc[:100000, :]
rating_2 = df[df['overall'] == 3].iloc[:100000, :]
rating_3 = df[df['overall'] == 2].iloc[:100000, :]
frames = [rating_1, rating_2, rating_3]
result = pd.concat(frames)
result = shuffle(result,random_state=0)
df = result


fig = plt.figure(figsize=(8,7))
colors=["coral","yellow","chartreuse"]
df['overall'].value_counts( sort=False).plot(kind = 'pie', autopct='%1.2f%%',fontsize=10 , startangle=90,colors=colors,counterclock=False)
plt.title('Rating')
plt.legend(labels=['1','2','3']) #colors --> party name
plt.tight_layout() #regularity
plt.show()


import random
from sklearn.utils import shuffle

import nltk
from nltk import FreqDist
import pandas as pd
pd.set_option("display.max_colwidth", 200)
import numpy as np
import re
import spacy

import gensim
from gensim import corpora

# libraries for visualization
import pyLDAvis
import pyLDAvis.gensim
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
pd.set_option("display.max_colwidth", 200)
import numpy as np
import re
import spacy

import gensim
from gensim import corpora

# libraries for visualization
import pyLDAvis
import pyLDAvis.gensim
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# function to plot most frequent terms
def freq_words(x, terms = 30):
  all_words = ' '.join([text for text in x])
  all_words = all_words.split()

  fdist = FreqDist(all_words)
  words_df = pd.DataFrame({'word':list(fdist.keys()), 'count':list(fdist.values())})

  # selecting top 20 most frequent words
  d = words_df.nlargest(columns="count", n = terms) 
  plt.figure(figsize=(20,5))
  ax = sns.barplot(data=d, x= "word", y = "count")
  ax.set(ylabel = 'Count')
  plt.show()

df["Text"]=df["Text"].astype(str)


freq_words(df['Text'])

# remove unwanted characters, numbers and symbols
df['Text'] = df['Text'].str.replace("[^a-zA-Z#]", " ")

from nltk.corpus import stopwords
stop_words = stopwords.words('english')


def remove_stopwords(rev):
    rev_new = " ".join([i for i in rev if i not in stop_words])
    return rev_new

# remove short words (length < 3)
df['Text'] = df['Text'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>2]))

# remove stopwords from the text
reviews = [remove_stopwords(r.split()) for r in df['Text']]

# make entire text lowercase
reviews = [r.lower() for r in reviews]



freq_words(reviews, 35)



nlp = spacy.load('en', disable=['parser', 'ner'])

def lemmatization(texts, tags=['NOUN', 'ADJ']): # filter noun and adjective
       output = []
       for sent in texts:
             doc = nlp(" ".join(sent)) 
             output.append([token.lemma_ for token in doc if token.pos_ in tags])
       return output


tokenized_reviews = pd.Series(reviews).apply(lambda x: x.split())
print(tokenized_reviews[1])


reviews_2 = lemmatization(tokenized_reviews)
print(reviews_2[1]) # print lemmatized review

reviews_3 = []
for i in range(len(reviews_2)):
    reviews_3.append(' '.join(reviews_2[i]))

df['reviews'] = reviews_3

freq_words(df['reviews'], 35)


dictionary = corpora.Dictionary(reviews_2)






