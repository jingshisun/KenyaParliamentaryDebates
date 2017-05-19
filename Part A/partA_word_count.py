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


def wordcount(years):
    ###### word count ######
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
    
    headers = ['year_of_debates','land', 'infrastructure', 'road[s]', 
               'school[s]', 'hospital[s]', 'disease', 'corruption', 'economy', 'tribe']
    
    # Write headers into output CSV file
    with open("wordcount.csv", "w", newline = '', encoding='utf-8') as f:
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
            
        # Write the word counts into a CSV file
        with open("wordcount.csv", "a", newline = '', encoding = 'utf-8') as f:
            writer = csv.DictWriter(f, fieldnames = headers)
            writer.writerow({'year_of_debates': str(year),
                             'land':land_count,
                             'infrastructure':infrastructure_count,
                             'road[s]':road_count,
                             'school[s]':school_count,
                             'hospital[s]':hospital_count,
                             'disease':disease_count,
                             'corruption':corruption_count,
                             'economy':economy_count,
                             'tribe':tribe_count})

            
def main():
    # set directory
    os.chdir("/Users/jingshisun/Desktop/KenyaParliamentaryDebates/sentiment")
    # specify the years 
    years = {1963, 1964, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1977, 1978, 1979, 1980, 1981, 1983, 1985, 1987, 1990, 1992, 1996, 1997, 1998, 1999, 2004, 2008}
    # calculate word counts
    wordcount(years)
    
        
if __name__ == "__main__":
    
    main()
