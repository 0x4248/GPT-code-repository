# Image Segmentation using K-means Clustering - 3841

**Language**: `C`

**Lines of code**: `115`

## Description

This program implements the K-means clustering algorithm to perform image segmentation. Image segmentation is the process of partitioning an image into multiple segments or regions to simplify the image analysis. K-means clustering is an unsupervised machine learning algorithm that groups similar data points together by minimizing the sum of squared distances between data points and their assigned cluster centers.

## Code

``` C
// Image Segmentation using K-means Clustering

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_ITERATIONS 100
#define NUM_CLUSTERS 3

typedef struct {
    float r, g, b;
} Pixel;

typedef struct {
    float r, g, b;
    int count;
} Cluster;

// Function to calculate Euclidean distance between two pixels
float calculate_distance(Pixel pixel1, Pixel pixel2) {
    float distance = sqrt(pow(pixel1.r - pixel2.r, 2) + pow(pixel1.g - pixel2.g, 2) + pow(pixel1.b - pixel2.b, 2));
    return distance;
}

// Function to assign pixels to the closest cluster
void assign_to_clusters(Pixel* pixels, Cluster* clusters, int num_pixels) {
    for (int i = 0; i < num_pixels; i++) {
        float min_distance = calculate_distance(pixels[i], clusters[0]);
        int min_cluster = 0;

        for (int j = 1; j < NUM_CLUSTERS; j++) {
            float distance = calculate_distance(pixels[i], clusters[j]);
            if (distance < min_distance) {
                min_distance = distance;
                min_cluster = j;
            }
        }

        clusters[min_cluster].r += pixels[i].r;
        clusters[min_cluster].g += pixels[i].g;
        clusters[min_cluster].b += pixels[i].b;
        clusters[min_cluster].count++;
    }
}

// Function to update the cluster centers
void update_cluster_centers(Cluster* clusters) {
    for (int i = 0; i < NUM_CLUSTERS; i++) {
        if (clusters[i].count > 0) {
            clusters[i].r /= clusters[i].count;
            clusters[i].g /= clusters[i].count;
            clusters[i].b /= clusters[i].count;
        }
    }
}

// Function to perform image segmentation using K-means clustering
void perform_segmentation(Pixel* pixels, int width, int height) {
    Cluster clusters[NUM_CLUSTERS];

    // Initialize cluster centers randomly
    for (int i = 0; i < NUM_CLUSTERS; i++) {
        clusters[i].r = (float)rand() / RAND_MAX;
        clusters[i].g = (float)rand() / RAND_MAX;
        clusters[i].b = (float)rand() / RAND_MAX;
        clusters[i].count = 0;
    }

    // Iterate until convergence or maximum iterations
    int iterations = 0;
    while (iterations < MAX_ITERATIONS) {
        assign_to_clusters(pixels, clusters, width * height);
        update_cluster_centers(clusters);
        iterations++;
    }

    // Assign each pixel to the cluster with the closest center
    for (int i = 0; i < width * height; i++) {
        float min_distance = calculate_distance(pixels[i], clusters[0]);
        int min_cluster = 0;

        for (int j = 1; j < NUM_CLUSTERS; j++) {
            float distance = calculate_distance(pixels[i], clusters[j]);
            if (distance < min_distance) {
                min_distance = distance;
                min_cluster = j;
            }
        }

        // Set pixel color based on the cluster center
        pixels[i].r = clusters[min_cluster].r;
        pixels[i].g = clusters[min_cluster].g;
        pixels[i].b = clusters[min_cluster].b;
    }
}

// Example usage
int main() {
    // Read image pixels (replace with your image loading logic)
    int width = 640;
    int height = 480;
    Pixel* pixels = (Pixel*)malloc(width * height * sizeof(Pixel));

    // Populate pixels with image data

    // Perform image segmentation
    perform_segmentation(pixels, width, height);

    // Process the segmented image (e.g., save, display, or further analysis)

    // Cleanup
    free(pixels);

    return 0;
}

```

## Prompt

```
Make me a program in C that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does. 
```