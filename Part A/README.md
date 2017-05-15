# Part A (results are in the output folder)
# Word Count

Method: use regular expression to extract specific words and count them.

# Sentiment Analysis

Matching Words with Emotions

The current study utilized the NRC Word-Emotion Association Lexicon database (Mohammad & Turney, 2013). The database provides a list of words from the Macquarie Thesaurus (Bernard, 1986) along with an indicator of whether or not the word is associated with any of eight emotions (anger, fear, anticipation, surprise, trust, sadness, joy, and disgust) and either positive or negative general sentiment (for a total of 10 variables per word). Note that it was possible for words to be associated with more than one emotion (e.g., both sadness and anger) though it was not possible to have more than one general sentiment (although the lack of a general sentiment was allowed).

Implementation

Since the NRC database does not include contractions (e.g., "isn't") it was important that all contractions were split into their component words (which was achieved through a text replacement algorithm). Further, the database only included root words (e.g., "dog" but not its plural "dogs") so the words needed to be lemmatized (i.e., reduced to their stem words) using the WordNet lemmatizer, which is available in the nltk Python module. Also, words that were negated (e.g., "not happy" should not be considered an indication of joy) were accounted for through the use of the mark_negation function in the nltk module (i.e., negated words were not counted towards any emotion). Lastly, the texts needed to be cleaned of punctuation marks, numbers, and superfluous white spaces. The number of words that were associated with each emotion were converted to emotion percentages (as based on the total number of words identified to be in the NRC database).