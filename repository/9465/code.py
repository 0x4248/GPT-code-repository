import pandas as pd
import random

# load dataset of songs
songs_df = pd.read_csv("songs_dataset.csv")

# define function to recommend a song
def recommend_song(genre, mood):
    # filter songs based on genre and mood
    filtered_songs = songs_df[(songs_df["genre"] == genre) & (songs_df["mood"] == mood)]
    # select a random song from the filtered list
    if len(filtered_songs) > 0:
        recommended_song = random.choice(filtered_songs["song_name"].values)
        return recommended_song
    else:
        return "Sorry, no songs match your preferences."

# prompt user for genre and mood inputs
user_genre = input("Enter your preferred genre: ")
user_mood = input("Enter your current mood: ")

# recommend a song based on user inputs
recommended_song = recommend_song(user_genre, user_mood)

# print the recommended song
print("We recommend:", recommended_song)
