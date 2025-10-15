#include <stdio.h>
#include <string.h>

// Function to build the LPS (Longest Prefix Suffix) array
void computeLPSArray(char* pattern, int m, int lps[]) {
    int length = 0; // length of the previous longest prefix suffix
    lps[0] = 0;     // lps[0] is always 0

    int i = 1;
    while (i < m) {
        if (pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
}

// KMP string matching function
void KMPsearch(char* text, char* pattern) {
    int n = strlen(text);
    int m = strlen(pattern);

    int lps[m];
    computeLPSArray(pattern, m, lps); // Preprocess the pattern

    int i = 0; // index for text[]
    int j = 0; // index for pattern[]

    printf("\nText: %s\n", text);
    printf("Pattern: %s\n\n", pattern);

    int found = 0;

    while (i < n) {
        if (pattern[j] == text[i]) {
            i++;
            j++;
        }

        if (j == m) {
            printf("Pattern found at index %d\n", i - j);
            j = lps[j - 1];
            found = 1;
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0)
                j = lps[j - 1];
            else
                i++;
        }
    }

    if (!found) {
        printf("Pattern not found in the text.\n");
    }
}

// Main function
int main() {
    char text[100], pattern[50];

    printf("Enter the text: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = 0; // Remove newline

    printf("Enter the pattern to search: ");
    fgets(pattern, sizeof(pattern), stdin);
    pattern[strcspn(pattern, "\n")] = 0; // Remove newline

    KMPsearch(text, pattern);

    return 0;
}