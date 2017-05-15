#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 17:08:42 2017

@author: jingshisun
"""

import glob
import os 
import re
import csv


def main():
    ###### word count ######
    
    # set directory
    os.chdir("/Users/jingshisun/Desktop/KenyaParliamentaryDebates/1963/1963")
    
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
            
    wordstring = wordstring.lower()
            
    # using regular expression to find the words and count them
    land_count = str(len(land.findall(wordstring)))
    infrastructure_count = str(len(infrastructure.findall(wordstring)))
    road_count= str(len(road.findall(wordstring)))
    school_count = str(len(school.findall(wordstring)))
    hospital_count = str(len(hospital.findall(wordstring)))
    disease_count = str(len(disease.findall(wordstring)))
    corruption_count= str(len(corruption.findall(wordstring)))
    economy_count = str(len(economy.findall(wordstring)))
    tribe_count=str(len(tribe.findall(wordstring)))
        
    headers = ['year of debates','land', 'infrastructure', 'road[s]', 
               'school[s]', 'hospital[s]', 'disease', 'corruption', 'economy', 'tribe']
    
    # Write headers into output CSV file
    with open("wordcount.csv", "w", newline = '', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = headers)
        writer.writeheader()    
    
    # Write the word counts into a CSV file
    with open("wordcount.csv", "a", newline = '', encoding = 'utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = headers)
        writer.writerow({'year of debates': '1963',
                         'land':land_count,
                         'infrastructure':infrastructure_count,
                         'road[s]':road_count,
                         'school[s]':school_count,
                         'hospital[s]':hospital_count,
                         'disease':disease_count,
                         'corruption':corruption_count,
                         'economy':economy_count,
                         'tribe':tribe_count})

        
if __name__ == "__main__":
    
    main()
