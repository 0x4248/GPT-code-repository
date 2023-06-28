# Movie Recommender System - 4624

**Language**: `Python`

**Lines of code**: `38`

## Description

This program is a movie recommender system that suggests movies to users based on their ratings of other movies. It uses a combination of collaborative filtering and content-based filtering to make recommendations.

## Code

``` Python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Load movie data
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Pivot the ratings data to create a user-movie matrix
user_movie_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating')

# Fill missing values with 0
user_movie_matrix = user_movie_matrix.fillna(0)

# Convert the user-movie matrix to a sparse matrix
sparse_matrix = csr_matrix(user_movie_matrix)

# Compute the cosine similarity matrix
similarity_matrix = cosine_similarity(sparse_matrix)

# Convert the similarity matrix to a pandas DataFrame
similarity_df = pd.DataFrame(similarity_matrix, index=user_movie_matrix.index, columns=user_movie_matrix.index)

# Define a function to get similar users
def similar_users(user_id):
    sim_users = similarity_df[user_id].sort_values(ascending=False)
    sim_users = sim_users.drop(user_id)
    return sim_users

# Define a function to get recommended movies
def recommend_movies(user_id, num_movies=5):
    sim_users = similar_users(user_id)
    movies = user_movie_matrix.loc[user_id]
    movies = movies[movies > 0].index
    
    sim_users_ratings = user_movie_matrix.loc[sim_users, movies

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```