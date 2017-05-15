#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 17:36:21 2017

@author: jingshisun
"""

import glob
import os 
import re


###### word count ######

# set directory
os.chdir("/Users/jingshisun/Desktop/KenyaParliamentaryDebates/1963")

# a string to record all words
wordstring =''

# regular expressions for the words to be counted 
land = re.compile("land")
infrastructure=re.compile("infrastructure")
road=re.compile("road|roads")
school=re.compile("school|schools")
hospital=re.compile("hospital|hospitals")
disease=re.compile("disease")
corruption=re.compile("corruption")
economy=re.compile("economy")
tribe=re.compile("tribe")

# read the two files under the folder 1963
read_files = glob.glob("*.txt")

# add them to the wordstring
for f in read_files:
    with open(f, "rb") as infile:
        wordstring+=str(infile.read())
        
# using regular expression to find the words and count them
with open('word_count.txt', 'w') as outfile:
    outfile.write('Count the number of times the following words were mentioned: land, infrastructure, road[s], school[s], hospital[s], disease, corruption, economy, tribe'+'\n\n')
    outfile.write('land'+'\t'+str(len(land.findall(wordstring)))+'\n')
    outfile.write('infrastructure'+'\t'+str(len(infrastructure.findall(wordstring)))+'\n')
    outfile.write('road[s]'+'\t'+str(len(road.findall(wordstring)))+'\n')
    outfile.write('school[s]'+'\t'+str(len(school.findall(wordstring)))+'\n')
    outfile.write('hospital[s]'+'\t'+str(len(hospital.findall(wordstring)))+'\n')
    outfile.write('disease'+'\t'+str(len(disease.findall(wordstring)))+'\n')
    outfile.write('corruption'+'\t'+str(len(corruption.findall(wordstring)))+'\n')
    outfile.write('economy'+'\t'+str(len(economy.findall(wordstring)))+'\n')
    outfile.write('tribe'+'\t'+str(len(tribe.findall(wordstring)))+'\n')



###### Sentiment analysis ######

#### Create a class that stores the NRC Word-Emotion Assocations dataset as a
#### a dictionary (once the word_association object is constructed), then 
#### provides the 'count_emotions' method to count the number occasions for 
#### emotion.
class word_assocations:
    
    def __init__(self):
        # Import NRC Word-Emotion Association data
        with open("NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt", "r", 
              newline = '', encoding = 'utf-8') as f:
            file = f.readlines()
        file = file[46:] # First 45 lines are comments

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





