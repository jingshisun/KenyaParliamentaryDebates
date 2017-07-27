"""
Created on Tue July 18
@author: arian1123
"""

import glob
import os
import re
import pandas as pd
from collections import Counter

years = {1963, 1964, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975,
         1977, 1978, 1979, 1980, 1981, 1983, 1985, 1987, 1990, 1992, 1996,
        1997, 1998, 1999, 2004, 2008, 2013, 2014, 2015, 2016, 2017}


#get all years there was a Parliamentary Election from excel file
def getElectionYears():

    xl = pd.ExcelFile("parliamentarians.xls")
    df = xl.parse()

    #get unique years
    years = set(df.year)

    #sort
    years = list(years)
    years.sort()

    return years

#end getParliamentaryYears

#get all MPs organized by year
def getMembers(year):

    #store both full name, as stored in excel file, and a parsed last name, as it may appear in parliamentary records
    members = {}
    members['full_name'] = []
    members['last_name'] = []

    xl = pd.ExcelFile("parliamentarians.xls")
    df = xl.parse()

    #get all MPs for the passed year
    mps = df[(df.year == year)]

    #store full names of MPs
    members['full_name'] = list(mps.candidate)

    #loop over full names, parse and add matching last names (estimated)
    for m in members['full_name']:

        m = m.lower()
        splitName = m.split(' ')

        # names of year in file are in last-name/first-name order
        # first token is last name, so take first token of full name string
        # if the first token is short, assume the full last name of MP is of format like 'De Souza'
        # so add 2nd token in full name string to last name
        # else just use first token
        if (year == 1963 or years == 1969 or year == 1974 or year == 1979 or year == 1983 or year == 2002 or year == 2007):
            if(len(splitName[0]) < 3):
                name = splitName[0] + " " + splitName[1]
            else:
                name = splitName[0]

        #if names are otherwise in firstname/lastname order then follow reserve logic
        else:
            if (len(splitName[-1]) < 3):
                name = splitName[-2] + " " + splitName[-1]
            else:
                name = splitName[-1]

        #add parsed name to list of last names
        members['last_name'].append(name)

    return members

#end getMemebers

#add all the year's speeches into one long string
def getSpeechText(year):

    totalString = ''

    path = "KenyanParliamentarySpeeches/" + str(year) + "/Output/*.txt"
    files = glob.glob(path)
    # add them to the wordstring
    for f in files:
        with open(f, "rb") as i:
            totalString += str(i.read())

    return totalString.lower().rstrip()

#end getSpeechText


def main():

    os.chdir("/Users/arianghashghai/Desktop/KenyanParliamentData/")

    electionYears = getElectionYears()

    #dictionary of MPs, year is key, dictionary of fullname/lastname is value
    members = {}

    #dictionary of years of parliamentary sessions, key is year, value is string of transcripts
    speeches = {}

    #iterate over election years, populate members
    for y in electionYears:

        m = getMembers(y)
        members[y] = m


    #iterate over speech years
    for y in years:

        with open('MPSpeakingCounts.txt', 'a') as outfile:
            outfile.write('\n\n' + str(y) + ': ')

        #get the matching election year for this year of speeches
        #election year must be equal or the current year, or then the next smallest year electionYears
        mpYear = [i for i in electionYears if i <= y][-1]

        #get matching MPs
        mps = members[mpYear]

        #get year's complete speech transcript
        text = getSpeechText(y)

        #get speaking counts
        for i, m in enumerate(mps['last_name']):

            #add : since assuming colon denotes speaker
            t = re.compile(m + ':')
            count = len(t.findall(text))

            if count > 0:
                with open('MPSpeakingCounts.txt', 'a') as outfile:
                    outfile.write(mps['full_name'][i] + ': ' + str(count) + ', ')


#end main

if __name__ == "__main__":
    main()
