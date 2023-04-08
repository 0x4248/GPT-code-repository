import nltk
import random
from nltk.corpus import movie_reviews

# Get the movie reviews dataset
nltk.download('movie_reviews')

# Create a list of tuples, where each tuple is a movie review and its sentiment (pos or neg)
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents to ensure a more even distribution of pos/neg reviews
random.shuffle(documents)

# Create a list of all words in the dataset
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

# Use the most common 3000 words as features
all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]

# Define a function to extract the features from a given review
def find_features(review):
    words = set(review)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

# Extract the features from the reviews and split the dataset into training and testing sets
featuresets = [(find_features(review), sentiment) for (review, sentiment) in documents]
train_set = featuresets[:1500]
test_set = featuresets[1500:]

# Train the classifier using the training set
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Test the classifier using the testing set
accuracy = nltk.classify.accuracy(classifier, test_set)
print("Accuracy:", accuracy)

# Test the classifier on some sample reviews
sample_reviews = ["This movie was amazing!", "I didn't like this movie at all.", "The acting was great but the plot was boring."]
for review in sample_reviews:
    print(review)
    features = find_features(review.split())
    sentiment = classifier.classify(features)
    print("Sentiment:", sentiment)
    print()
