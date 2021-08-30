# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Solution

In order to solve this problem, we will need to use Machine learning as well as an imported library to distinguish the words as positive or negative. The way this code will work is that it will search through the text looking for words with a positive meaning or negative meaning. Then the ratio of positive and negative sentiments will be determined. In the end, based on the data collected, the program will be able to calculate whether the main emotion in the text is positive or negative. 

I think that the overall sentiment of the text should be between postive and neutral. I think this because the text is just talking about a dream that a person had. They used a decent amount of words with positive meaning, and had some with a neautral meaning. Very little words with negative meanings.

Now onto the actual coding bit.

At first, I tried using java (as I have the most knowledge of it) to solve this problem. I would use the Stanford NLP library to assist me with building this program, however, the issue is that it will be complicated to use that library; therefore, I will use python instead with the help of the NLTK library. I do not have as much knowledge of python as I do java so this program may have some gaps in it.

I use the following playlist to make this program: https://www.youtube.com/watch?v=dyN_WtjdfpA&list=PLhTjy8cBISEoOtB5_nwykvB9wfEDscuEo

https://github.com/attreyabhatt/Sentiment-Analysis/blob/master/main.py

Method one (without the use of the NLTK library):
The very first thing to do is to save the text as a string, set the entire text to lowercase, remove the punctuation, and then tokenize the words (or separate the sentences into words). We will use the imported string library to help us do that. From there we remove the words with no meaning aka the stop words. After removing the stop words, we use the remaining words and see if they match up with any words found within the words in the emotions.txt file. If there is a match, the emotion that is associated with that word is added to the emotions_list and after the loop is completed the counter tallies the emotions and prints the results. From there one could create a graph, or use a mathematical representation to get the emotion ratio. 

Method two:
A much simpler method is possible through the use of the NLTK library. The first few steps are the same. We have to set it to lowercase and remove the strings with the help of the imported string library. Then comes in the NLTK library. After downloading and importing the libraries, I added a function called SentimentAnalysis. This function takes the cleaned text as a parameter, and scans through it, and determines the sentiment ratio. In the end, the function will print the ratio of negative, neutral, and positive sentiment and will also print the more apparent sentiment after comparing the ratios. It will print positive if the positive ratio is larger. If the negative sentiment ratio is larger, negative sentiment will be printed. If they are equal or there is some other scenario then a neutral sentiment is printed.

