#string import to remove punctuation and translate text into cleanedText
import string

#NLTK library that will be used
from nltk.corpus import stopwords
from nltk.corpus.reader.chasen import test
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


#text is stored in here
text = open('input.txt').read()

#changes all letters in the text to lowercase(to ensure that the words we are comparing are all the same case)
lower_case = text.lower()

"""Remove punctuations"""
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

#This function uses the sentiment analyzer to determine the sentiment score of the text and outputs the result
def SentimentAnalysis(analyze_text):
    score = SentimentIntensityAnalyzer().polarity_scores(analyze_text)
    neg = score['neg']
    pos = score['pos']
    neu = score['neu']
    print (score)
    if pos > neg :
        print("The text has a positve sentiment")
    elif neg > pos :
        print("The text has a negative sentiment")
    else:
        print("The text has a neutral sentiment")
    

SentimentAnalysis(cleaned_text)



