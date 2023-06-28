# Sentiment Analyzer - 1786

**Language**: `Python`

**Lines of code**: `26`

## Description

This program utilizes the Natural Language Toolkit (NLTK) library in Python to perform sentiment analysis on a given text. It uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon to assign sentiment scores to the text. The sentiment scores are then classified as either positive, negative, or neutral based on a threshold. The program allows the user to enter a text and displays the sentiment analysis result. It demonstrates the use of NLP techniques to evaluate the sentiment of textual data.

## Code

``` Python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        nltk.download('vader_lexicon')
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        sentiment_scores = self.sia.polarity_scores(text)
        compound_score = sentiment_scores['compound']
        
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

# Main program
analyzer = SentimentAnalyzer()

text = input("Enter text to analyze sentiment: ")
sentiment = analyzer.analyze_sentiment(text)

print("Sentiment: " + sentiment)

```

## Prompt

```

```