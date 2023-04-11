# Movie Recommendation System using Collaborative Filtering - 4547

**Language**: `Java`

**Lines of code**: `35`

## Description

This program is a movie recommendation system that uses collaborative filtering to recommend movies to users based on their previous movie ratings. The program takes a dataset of movie ratings from users and uses it to create a user-item matrix. It then calculates the similarity between users based on their movie ratings and recommends movies that similar users have rated highly.

## Code

``` Java
import java.io.File;
import java.io.IOException;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.neighborhood.NearestNUserNeighborhood;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;

public class MovieRecommender {

    public static void main(String[] args) throws IOException, TasteException {
        // Load data from file
        DataModel model = new FileDataModel(new File("data/movies.csv"));

        // Define similarity metric
        UserSimilarity similarity = new PearsonCorrelationSimilarity(model);

        // Define user neighborhood
        UserNeighborhood neighborhood = new NearestNUserNeighborhood(10, similarity, model);

        // Define recommender
        GenericUserBasedRecommender recommender = new GenericUserBasedRecommender(model, neighborhood, similarity);

        // Recommend items for user
        List<RecommendedItem> recommendations = recommender.recommend(1, 5);
        for (RecommendedItem recommendation : recommendations) {
            System.out.println(recommendation);
        }
    }
}

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.

Dont use python and no more than 100 lines of code
```