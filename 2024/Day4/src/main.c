#include <stdio.h>
#include <stdlib.h>

int get_line_length(const char *filename);
int get_rows(const char *filename);
char *get_char(char *word_search, int row, int col);
void init_word_search(char *word_search, const char *filename);
void print_field(char *word_search);

int ROWS;
int COLS;

int main(void) {
    const char filename[] = "input.txt";
    COLS = get_line_length(filename);
    ROWS = get_rows(filename);
    char *word_search = malloc(ROWS * COLS * sizeof(char));

    init_word_search(word_search, filename);
    print_field(word_search);

    return 0;
}

int get_line_length(const char *filename) {
    int length = 0;
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Opening file failed");
        exit(1);
    }
    char c;

    while ((c = fgetc(file)) != '\n') {
        length++;
    }

    fclose(file);
    return length;
}

int get_rows(const char *filename) {
    int rows = 0;
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Opening file failed");
        exit(1);
    }
    char c;

    while ((c = fgetc(file)) != EOF) {
        if (c == '\n') {
            rows++;
        }
    }

    fclose(file);
    return rows;
}

char *get_char(char *word_search, int row, int col) { return &word_search[row * ROWS + col]; }

void print_field(char *word_search) {
    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
            printf("[%c]", *get_char(word_search, row, col));
        }
        printf("\n");
    }
}

void init_word_search(char *word_search, const char *filename) {
    char buffer[COLS];
    int current_row = 0;
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Opening file failed");
        exit(1);
    }

    while (fgets(buffer, COLS+2, file)) {
        for (int i = 0; i < COLS; i++) {
            if (buffer[i] != '\n' && buffer[i] != '\0' && buffer[i] != '\r') {
                *get_char(word_search, current_row, i) = buffer[i];
            }
        }
        current_row++;
    }
}
