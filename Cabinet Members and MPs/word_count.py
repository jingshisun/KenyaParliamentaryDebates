#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 15:55:19 2017

@author: jingshisun
"""


##############################################################################################
import glob
import os 
import re
import pandas as pd
#import xlrd
os.chdir("/Users/jingshisun/Desktop/KenyaParliamentaryDebates/sentiment")
df = pd.read_excel("../Cabinet Members and MPs/constituency.xlsx")
# specify the years 
years = {1963, 1964, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 
         1977, 1978, 1979, 1980, 1981, 1983, 1985, 1987, 1990, 1992, 1996, 
         1997, 1998, 1999, 2004, 2008, 2013, 2014, 2015}


for year in years:
    
    with open('constituency_count.txt', 'a') as outfile:
         outfile.write('\n\n'+str(year)+': ')
        
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
        regex = re.compile(i.lower())
        count = str(len(regex.findall(wordstring)))
        if count != '0': 
            #print (year +' '+ i + ' '+count)
            with open('constituency_count.txt', 'a') as outfile:
                outfile.write(i + ': ' + count + ', ')
            
                

##############################################################################################
os.chdir("/Users/jingshisun/Desktop/KenyaParliamentaryDebates/sentiment")
xl = pd.ExcelFile("../Cabinet Members and MPs/Kenya Cabinet Members.xls")
#xl.sheet_names
df = xl.parse("Kenyatta's Cabinet" and "Moi's Cabinet" and "Mwai Kibaki's Cabinet")
df1 = xl.parse("Kenyatta's Cabinet")
df2 = xl.parse("Moi's Cabinet")
df3 = xl.parse("Mwai Kibaki's Cabinet")
#df.head()
members =[]
i = 0
for col in df1.columns:
    if i % 2 != 0: 
        for member in df1[col]:
            members.append(member)
    i+=1
i = 0
for col in df2.columns:
    if i % 2 != 0: 
        for member in df2[col]:
            members.append(member)
    i+=1
i = 0
for col in df3.columns:
    if i % 2 != 0: 
        for member in df3[col]:
            members.append(member)
    i+=1


# remove nan values
cleanedList = [x for x in members if str(x) != 'nan']

# extract unique values of members' names
uniqueSet = set(cleanedList)

# specify the years 
years = {1963, 1964, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 
         1977, 1978, 1979, 1980, 1981, 1983, 1985, 1987, 1990, 1992, 1996, 
         1997, 1998, 1999, 2004, 2008, 2013, 2014, 2015}


for year in years:
    
    with open('cabinet_ministers_count.txt', 'a') as outfile:
         outfile.write('\n\n'+str(year)+': ')
        
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

    for member in uniqueSet:
        regex = re.compile(member.lower())
        count = str(len(regex.findall(wordstring)))
        if count != '0': 
            #print (year +' '+ i + ' '+count)
            with open('cabinet_ministers_count.txt', 'a') as outfile:
                outfile.write(member + ': ' + count + ', ')

                
##############################################################################################
