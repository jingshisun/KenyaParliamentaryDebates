#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 00:12:21 2017

@author: jingshisun
"""

import glob
import os 
import re
import nltk
from gensim import corpora, models
import gensim
from stop_words import get_stop_words
from nltk.tokenize import RegexpTokenizer




### Create function to lemmatize (stem) words to their root
### This requires the NLTK wordnet dataset.

def lemmatize_words(text):
    # Create a lemmatizer object
    wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()
    out = []
    for word in text:
        word = ''.join(w.lower() for w in word if w.isalpha())
        out.append(wordnet_lemmatizer.lemmatize(word))
    return(out)
    
def find_topic(raw_text):
    texts = []
    raw_text = raw_text.lower()
    tokens = lemmatize_words(raw_text.split())
    # remove stop words from tokens
    stopped_tokens = [j for j in tokens if not j in en_stop]
    texts.append(stopped_tokens)
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]
    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary, passes=20)
    print(ldamodel.print_topics(num_topics=-1, num_words=20))
    

def main():
    tokenizer = RegexpTokenizer(r'\w+')
    # create English stop words list
    en_stop = get_stop_words('en')
    find_topic("replace this sentence with any sentence here to find its topic")

if __name__ == "__main__":
    
    main()

    