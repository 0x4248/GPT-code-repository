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
