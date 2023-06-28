# Song Recommendation Engine - 9465

**Language**: `Python`

**Lines of code**: `26`

## Description

This program takes in a user's preferred genre and mood, and recommends a song based on those inputs. It uses an external dataset of songs with associated genres and moods to generate the recommendation.

This program loads a dataset of songs in CSV format and defines a function recommend_song that takes in a user's preferred genre and mood and returns a song recommendation based on those inputs. It filters the dataset based on the genre and mood inputs, selects a random song from the filtered list, and returns it as the recommendation. If no songs match the user's preferences, it returns an error message.

The program prompts the user to enter their preferred genre and mood, calls the recommend_song function with those inputs, and prints the recommended song. The output is the recommended song name.

This program uses pandas library to read the CSV file and manipulate the data. It also uses the random module to randomly select a song from the filtered list. The program can be easily extended by adding more features such as artist name, album name, and so on.

## Code

``` Python
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

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```