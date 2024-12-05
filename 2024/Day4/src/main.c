#include <stdio.h>
#include <stdlib.h>

int get_line_length(const char *filename);
int get_rows(const char *filename);
char *get_char(char *word_search, int row, int col);
void init_word_search(char *word_search, const char *filename);
void print_field(char *word_search);
int horizontal(char *word_search);
int vertical(char *word_search);
int diagonal_rtl(char *word_search);
int diagonal_ltr(char *word_search);

int ROWS;
int COLS;

int main(void) {
    const char filename[] = "input.txt";
    COLS = get_line_length(filename);
    ROWS = get_rows(filename);
    char *word_search = malloc(ROWS * COLS * sizeof(char));

    init_word_search(word_search, filename);
    printf(
        "%d\n", vertical(word_search) + horizontal(word_search) + diagonal_ltr(word_search) +
                    diagonal_rtl(word_search)
    );

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

int horizontal(char *word_search) {
    int count = 0;
    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; (col + 3) < COLS; col++) {
            if (*get_char(word_search, row, col) == 'X' &&
                *get_char(word_search, row, col + 1) == 'M' &&
                *get_char(word_search, row, col + 2) == 'A' &&
                *get_char(word_search, row, col + 3) == 'S') {

                count++;
            } else if (*get_char(word_search, row, col) == 'S' &&
                       *get_char(word_search, row, col + 1) == 'A' &&
                       *get_char(word_search, row, col + 2) == 'M' &&
                       *get_char(word_search, row, col + 3) == 'X') {

                count++;
            }
        }
    }
    return count;
}

int vertical(char *word_search) {
    int count = 0;
    for (int row = 0; (row + 3) < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
            if (*get_char(word_search, row, col) == 'X' &&
                *get_char(word_search, row + 1, col) == 'M' &&
                *get_char(word_search, row + 2, col) == 'A' &&
                *get_char(word_search, row + 3, col) == 'S') {

                count++;
            } else if (*get_char(word_search, row, col) == 'S' &&
                       *get_char(word_search, row + 1, col) == 'A' &&
                       *get_char(word_search, row + 2, col) == 'M' &&
                       *get_char(word_search, row + 3, col) == 'X') {

                count++;
            }
        }
    }
    return count;
}

int diagonal_rtl(char *word_search) {
    int count = 0;
    for (int row = 0; (row + 3) < ROWS; row++) {
        for (int col = 0; (col + 3) < COLS; col++) {
            if (*get_char(word_search, row, col) == 'X' &&
                *get_char(word_search, row + 1, col + 1) == 'M' &&
                *get_char(word_search, row + 2, col + 2) == 'A' &&
                *get_char(word_search, row + 3, col + 3) == 'S') {

                count++;
            } else if (*get_char(word_search, row, col) == 'S' &&
                       *get_char(word_search, row + 1, col + 1) == 'A' &&
                       *get_char(word_search, row + 2, col + 2) == 'M' &&
                       *get_char(word_search, row + 3, col + 3) == 'X') {

                count++;
            }
        }
    }
    return count;
}

int diagonal_ltr(char *word_search) {
    int count = 0;
    for (int row = 0; (row + 3) < ROWS; row++) {
        for (int col = COLS; (col - 3) >= 0; col--) {
            if (*get_char(word_search, row, col) == 'X' &&
                *get_char(word_search, row + 1, col - 1) == 'M' &&
                *get_char(word_search, row + 2, col - 2) == 'A' &&
                *get_char(word_search, row + 3, col - 3) == 'S') {

                count++;
            } else if (*get_char(word_search, row, col) == 'S' &&
                       *get_char(word_search, row + 1, col - 1) == 'A' &&
                       *get_char(word_search, row + 2, col - 2) == 'M' &&
                       *get_char(word_search, row + 3, col - 3) == 'X') {

                count++;
            }
        }
    }
    return count;
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

char *get_char(char *word_search, int row, int col) { return &word_search[row * COLS + col]; }

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

    while (fgets(buffer, COLS + 2, file)) {
        for (int i = 0; i < COLS; i++) {
            if (buffer[i] != '\n' && buffer[i] != '\0' && buffer[i] != '\r') {
                *get_char(word_search, current_row, i) = buffer[i];
            }
        }
        current_row++;
    }
}
