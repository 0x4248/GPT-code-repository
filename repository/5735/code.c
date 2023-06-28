#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORD_LENGTH 100

struct word_count {
    char *word;
    int count;
};

int main() {
    char filename[MAX_WORD_LENGTH];
    printf("Enter the name of the text file: ");
    scanf("%s", filename);

    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error: Could not open file.\n");
        return 1;
    }

    int num_words = 0;
    struct word_count *word_counts = NULL;

    char buffer[MAX_WORD_LENGTH];
    while (fscanf(file, "%s", buffer) == 1) {
        // Convert word to lowercase
        for (int i = 0; buffer[i]; i++) {
            buffer[i] = tolower(buffer[i]);
        }

        // Check if word is already in word_counts
        int found = 0;
        for (int i = 0; i < num_words; i++) {
            if (strcmp(word_counts[i].word, buffer) == 0) {
                word_counts[i].count++;
                found = 1;
                break;
            }
        }

        // If word is not in word_counts, add it
        if (!found) {
            num_words++;
            word_counts = realloc(word_counts, num_words * sizeof(struct word_count));
            word_counts[num_words - 1].word = malloc(strlen(buffer) + 1);
            strcpy(word_counts[num_words - 1].word, buffer);
            word_counts[num_words - 1].count = 1;
        }
    }

    // Sort word_counts by frequency count in descending order
    for (int i = 0; i < num_words - 1; i++) {
        for (int j = i + 1; j < num_words; j++) {
            if (word_counts[i].count < word_counts[j].count) {
                struct word_count temp = word_counts[i];
                word_counts[i] = word_counts[j];
                word_counts[j] = temp;
            }
        }
    }

    // Print word frequency count
    printf("Word frequency count:\n");
    for (int i = 0; i < num_words; i++) {
        printf("%s: %d\n", word_counts[i].word, word_counts[i].count);
    }

    // Free memory
    for (int i = 0; i < num_words; i++) {
        free(word_counts[i].word);
    }
    free(word_counts);

    fclose(file);
    return 0;
}
