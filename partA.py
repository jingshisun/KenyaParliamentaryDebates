#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 17:36:21 2017

@author: jingshisun
"""

import glob
import os 
import re




# set directory
os.chdir("/Users/jingshisun/Desktop/KenyaParliamentaryDebates/1963")

wordstring =''

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

for f in read_files:
    with open(f, "rb") as infile:
        wordstring+=str(infile.read())
        
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
    
#len(land.findall(wordstring))
#len(infrastructure.findall(wordstring))
#len(road.findall(wordstring))
#len(school.findall(wordstring))
#len(hospital.findall(wordstring))
#len(disease.findall(wordstring))
#len(corruption.findall(wordstring))
#len(economy.findall(wordstring))
#len(tribe.findall(wordstring))




