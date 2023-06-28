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
