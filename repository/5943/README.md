# Sentiment Analyzer: Unleashing Emotion Insights - 5943

**Language**: `Python`

**Lines of code**: `33`

## Description

This program, written in Python, utilizes natural language processing techniques to analyze the sentiment of text input, providing valuable insights into the emotions expressed. It employs a pre-trained sentiment analysis model and incorporates additional features for enhancing its functionality. The program showcases the complexity of sentiment analysis and offers an interesting application of machine learning in understanding human emotions.

## Code

``` Python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    
    if sentiment_scores["compound"] >= 0.05:
        return "Positive"
    elif sentiment_scores["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Welcome to Sentiment Analyzer!")
    print("Enter a text to analyze its sentiment (press 'q' to quit):")
    
    while True:
        user_input = input("> ")
        
        if user_input.lower() == "q":
            break
        
        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}\n")
    
    print("Thank you for using Sentiment Analyzer!")

if __name__ == "__main__":
    main()

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```