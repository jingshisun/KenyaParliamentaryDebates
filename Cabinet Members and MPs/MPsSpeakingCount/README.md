Comments to this program:

The biggest issue stems from inconsistencies in from the input parliamentarians.xls file. Since the names of MPs are not clearly divided into first names and last names, these needs to be parsed in the program. Retrieving a last name of the MP was important, since first names are usually not used in the hansards to denote a speaker.

Looking through the file manually it also seems there was inconsistency for each year how the names were ordered. Some years appeared to have first name/last name order and some in reverse. The program added logic to try to handle this. To identify the order of names in year was done by personal judgement and research, so there may be misjudgments.

If the ordered of a name in the file was last name/first name (i.e. Miller Bob) we would pull the first token of the string and assume it be the last name of the MP. If the first token was shorter than 3 chars, we would also add the following token to the last name (for names such as "De Souza").

When running regex to retrieve counts, we checked the last names followed by a colon, since on optical inspection of the hansards the beginning of speaker's speech would usually be denoted in the format [title][last_name]:. This would also ensure we don't over-count, for instance if one MP mentions another in their speech, or other faulty pattern recognitions. 

It must be noted that this is an imperfect solution. Idiosyncrasies in the hansards cannot be accounted for, and cases such as MPs that share the same last name cannot be distinguished.

To minimize this error, when checking the speeches from a certain year we check only that the active MPs in that year (i.e. if we check speeches from 1964, we will only check the MPs elected to parliament in 1963, the most recent election year to 1964). Duplicate last names are less likely within one year than they are over a span over 40+ years.
