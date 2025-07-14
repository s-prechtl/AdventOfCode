#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#define STB_DS_IMPLEMENTATION
#include "stb_ds.h"

#define BUFFER_SIZE 1024
#define BLINKS 3

char **str_split(char *a_str, const char a_delim);
void read_stones_from_file(unsigned long long **stones, const char *filename);
void print_arr(unsigned long long *arr);
void blink(unsigned long long *stones);

int main(void) {
    const char filename[] = "input.txt";
    unsigned long long *stones = NULL;
    read_stones_from_file(&stones, filename);
    for (int i = 0; i < BLINKS; i++) {
        blink(stones);
    }

    printf("lel: %td", arrlen(stones));

    arrfree(stones);
    return 0;
}

void blink(unsigned long long *stones) {
    for (int i = 0; i < arrlen(stones); i++) {
        print_arr(stones);
        int number = stones[i];
        if (number == 0) {
            stones[i] = 1;
            print_arr(stones);
            continue;
        }

        char *number_string = malloc(BUFFER_SIZE);
        sprintf(number_string, "%d", number);
        int number_len = strlen(number_string);
        if (number_len % 2 == 0) {
            char left[number_len / 2 + 1];
            char right[number_len / 2 + 1];

            strncpy(left, number_string, number_len / 2);
            strncpy(right, number_string + number_len / 2, number_len / 2);

            left[number_len / 2] = '\0';
            right[number_len / 2] = '\0';

            long number_left = atoi(left);
            long number_right = atoi(right);
            if ((number_left == 0 && left[0] != '0') || (number_right == 0 && right[0] != '0')) {
                perror("Number couldn't be converted.");
                exit(1);
            }

            stones[i] = number_left;
            arrins(stones, i + 1, number_right);
            i++; // Skip the inserted element in this loop
        } else {
            stones[i] *= 2024;
        }
        print_arr(stones);
        free(number_string);
    }
}

void read_stones_from_file(unsigned long long **stones, const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Couldnt read input file!");
        return;
    }

    char *buffer = malloc(BUFFER_SIZE);

    while (fgets(buffer, BUFFER_SIZE, file)) {
        char **tokens = str_split(buffer, ' ');
        for (int i = 0; *(tokens + i); i++) {
            arrput(*stones, atoi(tokens[i]));
        }
    }

    free(buffer);
}

void print_arr(unsigned long long *arr) {
    printf("[");
    for (int i = 0; i < arrlen(arr); i++) {
        printf("%lld", arr[i]);
        if (i != (arrlen(arr) - 1)) {
            printf(", ");
        }
    }
    printf("]\n");
}

char **str_split(char *a_str, const char a_delim) {
    char **result = 0;
    size_t count = 0;
    char *tmp = a_str;
    char *last_comma = 0;
    char delim[2];
    delim[0] = a_delim;
    delim[1] = 0;

    /* Count how many elements will be extracted. */
    while (*tmp) {
        if (a_delim == *tmp) {
            count++;
            last_comma = tmp;
        }
        tmp++;
    }

    /* Add space for trailing token. */
    count += last_comma < (a_str + strlen(a_str) - 1);

    /* Add space for terminating null string so caller
       knows where the list of returned strings ends. */
    count++;

    result = malloc(sizeof(char *) * count);

    if (result) {
        size_t idx = 0;
        char *token = strtok(a_str, delim);

        while (token) {
            assert(idx < count);
            *(result + idx++) = strdup(token);
            token = strtok(0, delim);
        }
        assert(idx == count - 1);
        *(result + idx) = 0;
    }

    return result;
}
