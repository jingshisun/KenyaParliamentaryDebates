#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:44:49 2017

@author: jingshisun
"""

import glob
import os 
import re
import pandas as pd

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
    tokenizer = RegexpTokenizer(r'\w+')
    # create English stop words list
    en_stop = get_stop_words('en')
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
    return(ldamodel.print_topics(num_topics=-1, num_words=10))
    

def main():

    os.chdir("/Users/jingshisun/Desktop/KenyaParliamentaryDebates/sentiment")
    df = pd.read_excel("../Cabinet Members and MPs/constituency.xlsx")
    # specify the years 
    years = {1963, 1964, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 
            1977, 1978, 1979, 1980, 1981, 1983, 1985, 1987, 1990, 1992, 1996, 
            1997, 1998, 1999, 2004, 2008, 2013, 2014, 2015}
    
    #years = {1963}
    
    
    for year in years:
        
        #with open('constituency_topic.txt', 'a') as outfile:
        #     outfile.write('\n\n'+str(year)+': ')
            
        # a string to record all words
        wordstring =''
        year = str(year)
        path = "FlatWorldFiles/"+year+"/Output/*.txt"
        # read the two files under the folder 1963
        read_files = glob.glob(path)
        # add them to the wordstring
        for f in read_files:
            with open(f, "rb") as infile:
                wordstring+=str(infile.read())
    
        wordstring = wordstring.lower()
        
        for i in df['constituency'].unique():
            regex = re.compile("([^.]*?" + i.lower() + "[^.]*\.)")
            sentences = regex.findall(wordstring)
            
            count = len(sentences)
            if count != 0: 
                paragraph = ""
                for s in sentences: 
                    paragraph += s
                topic = find_topic(paragraph)
                #print(topic)
                #print(topic[0][1])
                
                with open('constituency_topic.txt', 'a') as outfile:
                    outfile.write('\n'+ str(year)+', ' + i + ': ' + topic[0][1])
                #break

if __name__ == "__main__":
    
    main()
