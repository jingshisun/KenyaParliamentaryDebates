#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 16:45:50 2017

@author: jingshisun
"""

import glob
import os 
import re
import nltk
from nltk.sentiment.util import mark_negation
import csv



        
### Create function to break apart contractions to its derivative words
### A text file containing this('contractions.txt') should be located at the 
### working directory along with this script.

def break_contractions(text):
    #### Import dictionary of contractions: contractions.txt
    with open('contractions.txt','r') as inf:
        contractions = eval(inf.read())
    
    pattern = re.compile(r'\b(' + '|'.join(contractions.keys()) + r')\b')
    result = pattern.sub(lambda x: contractions[x.group()], text)
    return(result)

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
    
#### Create function to remove stopwords (e.g., and, if, to)
#### Removes stopwords from a list of words (i.e., to be used on lyrics after splitting).
#### This requires the NLTK stopwords dataset.
def remove_stopwords(text):
    # Create set of all stopwords
    stopword_set = set(w.lower() for w in nltk.corpus.stopwords.words())
    out = []
    for word in text:
        # Convert words to lower case alphabetical letters only
        # word = ''.join(w.lower() for w in word if w.isalpha())
        if word not in stopword_set:
            out.append(word)
    # Return only words that are not stopwords
    return(out)
    

#### Create a class that stores the NRC Word-Emotion Assocations dataset as a
#### a dictionary (once the word_association object is constructed), then 
#### provides the 'count_emotions' method to count the number occasions for 
#### emotion.
class word_assocations:
    
    def __init__(self):
        # Import NRC Word-Emotion Association data
        with open("NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt", "r", newline = '', encoding = 'utf-8') as f:
            file = f.readlines()
        file = file[2:] # First 2 lines are comments

        # Create dictionary with words and their associated emotions
        associations = {}
        for line in file:
            elements = line.split()
            if elements[2] == '1':
                if elements[0] in associations:
                    associations[elements[0]].append(elements[1])
                else:
                    associations[elements[0]] = [elements[1]]

        # Initializes associations dictionary (so not to repeat it)
        self.associations = associations

    def count_emotions(self, text):
         # Clean up the string of characters
        temp0 = break_contractions(text)                                         # Break up contractions
        temp1 = lemmatize_words(temp0.split())                                   # Split string to words, then lemmatize
        temp2 = mark_negation(temp1, double_neg_flip = True)                     # Account for negations
        temp3 = remove_stopwords(temp2)                                          # Remove any stopwords
        
        # check_spelling(temp2)  # Function is no longer useful
        
        # Count number of emotional associations for each valid word
        bank = []
        wordcount = 0
        for word in temp3:
            if word in self.associations:
               bank.extend(self.associations[word])
               wordcount += 1

        # Returns a tuple of integers for negative, positive, anger, fear, anticipation,
        # surprise, trust, sadness, joy, disgust, and total word count, respectively.
        return((bank.count('negative'),
                bank.count('positive'),
                bank.count('anger'),
                bank.count('fear'),
                bank.count('anticipation'),
                bank.count('surprise'),
                bank.count('trust'),
                bank.count('sadness'),
                bank.count('joy'), 
                bank.count('disgust'),
                wordcount))       
                
                
def emotions(years):

    
    associator = word_assocations()

    headers = ['year_of_debates','negative', 'positive', 'anger', 
               'fear', 'anticipation', 'surprise', 'trust', 'sadness', 'joy', 
               'disgust', 'wordcount', 'negative_percent', 'positive_percent',
               'anger_percent', 'fear_percent', 'anticipation_percent',
               'surprise_percent', 'trust_percent', 'sadness_percent', 'joy_percent',
               'disgust_percent']
    
    #Write headers into output CSV file
    with open("sentiments.csv", "w", newline = '', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = headers)
        writer.writeheader()
        
    
    
    for year in years:
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
        
        wordstring=wordstring.lower()
        temp_emotions = associator.count_emotions(wordstring)
        if temp_emotions[0] > 0:
            negative_percent    = temp_emotions[0] / temp_emotions[10]
            positive_percent    = temp_emotions[1] / temp_emotions[10]
            anger_percent       = temp_emotions[2] / temp_emotions[10]
            fear_percent        = temp_emotions[3] / temp_emotions[10]
            anticipation_percent= temp_emotions[4] / temp_emotions[10]
            surprise_percent    = temp_emotions[5] / temp_emotions[10]
            trust_percent       = temp_emotions[6] / temp_emotions[10]
            sadness_percent     = temp_emotions[7] / temp_emotions[10]
            joy_percent         = temp_emotions[8] / temp_emotions[10]
            disgust_percent     = temp_emotions[9] / temp_emotions[10]
            with open("sentiments.csv", "a", newline = '', encoding = 'utf-8') as f:
                writer = csv.DictWriter(f, fieldnames = headers)
                writer.writerow({'year_of_debates': str(year),
                                 'negative': temp_emotions[0],
                                 'positive': temp_emotions[1],
                                 'anger': temp_emotions[2],
                                 'fear': temp_emotions[3],
                                 'anticipation': temp_emotions[4],
                                 'surprise': temp_emotions[5],
                                 'trust': temp_emotions[6],
                                 'sadness': temp_emotions[7],
                                 'joy': temp_emotions[8],
                                 'disgust': temp_emotions[9],
                                 'wordcount': temp_emotions[10], 
                                 'negative_percent': negative_percent,
                                 'positive_percent': positive_percent,
                                 'anger_percent': anger_percent,
                                 'fear_percent': fear_percent,
                                 'anticipation_percent': anticipation_percent,
                                 'surprise_percent': surprise_percent,
                                 'trust_percent': trust_percent,
                                 'sadness_percent': sadness_percent,
                                 'joy_percent': joy_percent,
                                 'disgust_percent': disgust_percent})

            
            
def main():
    
    # set directory
    os.chdir("/Users/jingshisun/Desktop/KenyaParliamentaryDebates/sentiment")
    # specify the years of the files to calculate
    years = {1963, 1964, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 
             1977, 1978, 1979, 1980, 1981, 1983, 1985, 1987, 1990, 1992, 1996, 
             1997, 1998, 1999, 2004, 2008, 2013, 2014, 2015}       
    # calculate sentiments based on NRC Emotion and Sentiment Lexicons
    emotions(years)
    
            
if __name__ == "__main__":
    
    main()


