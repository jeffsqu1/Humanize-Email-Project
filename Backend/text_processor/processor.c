#include "processor.h"
#include <string.h>
#include <ctype.h>

void clean_text(const char* input, char* output, int max_len){
    int i = 0, j = 0;
    int last_was_space = 0; // Flag to track whether last character was space

    while (input[i] != '\0' && j < max_len - 1){
        if (isspace((unsigned char)input[i])){ // Check current character [i]
            if (!last_was_space){
                output[j++] = ' '; // Add a space
                last_was_space = 1; // Set flag
            }
        } else {
            output[j++] = input[i]; // Add character
            last_was_space = 0; // Reset flag
        }
        i++;
    }
    output[j] = '\0'; // End output string
}

int word_count(const char* text){
    int count = 0, in_word = 0;
    for (int i = 0; text[i] != '\0'; i++){
        if (isspace((unsigned char)text[i])){
            in_word = 0;
        } else if (!in_word){
            in_word = 1;
            count++;
        }
    }
    return count;
}