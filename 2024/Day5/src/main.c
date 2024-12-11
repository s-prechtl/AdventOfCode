#include <stdio.h>
#include <stdlib.h>

#define STB_DS_IMPLEMENTATION
#include "stb_ds.h"

#define BUFFER_SIZE 1023

typedef struct PageOrderingRules {
    int key;
    int *value;

} PageOrderingRules;

void read_por_from_file(PageOrderingRules **pageOrderingRules, const char *filename);
void read_updates_from_file(int ***updates, const char *filename);
void print_por(PageOrderingRules *pageOrderingRules);
void print_updates(int **updates);
char **str_split(char *a_str, const char a_delim);
int in_array(int *arr, int i);
void print_arr(int *arr);
void print_arr_with_highlighted_element(int *arr, int el);

int main(void) {
    const char filename[] = "input.txt";
    PageOrderingRules *pageOrderingRules = NULL;
    int **updates = NULL;
    int sum = 0;
    read_por_from_file(&pageOrderingRules, filename);
    read_updates_from_file(&updates, filename);
    print_por(pageOrderingRules);

    for (int i = 0; i < arrlen(updates); i++) {
        int is_valid = 1;
        int *current_updates = updates[i];
        for (int j = 0; j < arrlen(current_updates) && is_valid; j++) {
            int current_page = current_updates[j];
            for (int k = j + 1; k < arrlen(current_updates) && is_valid; k++) {
                if (in_array(hmget(pageOrderingRules, current_updates[k]), current_page)) {
                    printf(
                        "Element %d is in %d's array of rules: ", current_page, current_updates[k]
                    );
                    print_arr_with_highlighted_element(
                        hmget(pageOrderingRules, current_updates[k]), current_page
                    );
                    printf("\n");
                    is_valid = 0;
                    break;
                }
            }
        }

        if (is_valid) {
            int middle = current_updates[arrlen(current_updates) / 2];
            sum += middle;
        }
    }

    printf("Sum: %d\n", sum);

    for (int i = 0; i < hmlen(pageOrderingRules); i++) {
        arrfree(pageOrderingRules[i].value);
    }
    hmfree(pageOrderingRules);

    for (int i = 0; i < arrlen(updates); i++) {
        arrfree(updates[i]);
    }
    arrfree(updates);

    return 0;
}

void print_arr_with_highlighted_element(int *arr, int el) {
    printf("[");
    for (int i = 0; i < arrlen(arr); i++) {
        if (arr[i] == el) {
            printf("\x1b[31m%d\x1b[39;49m", arr[i]);
        } else {
            printf("%d", arr[i]);
        }
        if (i != (arrlen(arr) - 1)) {
            printf(", ");
        }
    }
    printf("]");
}

void print_arr(int *arr) {
    printf("[");
    for (int i = 0; i < arrlen(arr); i++) {
        printf("%d", arr[i]);
        if (i != (arrlen(arr) - 1)) {
            printf(", ");
        }
    }
    printf("]");
}

int in_array(int *arr, int el) {
    for (int i = 0; i < arrlen(arr); i++) {
        if (arr[i] == el) {
            return 1;
        }
    }
    return 0;
}

void print_updates(int **updates) {
    for (int i = 0; i < arrlen(updates); i++) {
        print_arr(updates[i]);
        printf("\n");
    }
}

void read_updates_from_file(int ***updates, const char *filename) {
    FILE *file = fopen(filename, "r");

    if (!file) {
        perror("Could not open file!");
        exit(1);
    }

    char *buffer = malloc(BUFFER_SIZE);
    int is_updates = 0;

    while (fgets(buffer, BUFFER_SIZE, file)) {
        if (buffer[0] == '\n') {
            is_updates = 1;
            continue;
        }
        if (!is_updates) {
            continue;
        }
        char **tokens = str_split(buffer, ',');
        int *values = NULL;
        if (arrlen(tokens) > 0) {
            for (int i = 0; *(tokens + i); i++) {
                arrput(values, atoi(tokens[i]));
            }
            if (arrlen(values) > 0) {
                arrput(*updates, values);
            }
        }
    }
}

void read_por_from_file(PageOrderingRules **pageOrderingRules, const char *filename) {
    FILE *file = fopen(filename, "r");

    if (!file) {
        perror("Could not open file!");
        exit(1);
    }

    char *buffer = malloc(BUFFER_SIZE);

    while (fgets(buffer, BUFFER_SIZE, file)) {
        if (buffer[0] == '\n') {
            break;
        }

        char **tokens = str_split(buffer, '|');
        if (tokens) {
            int key = atoi(tokens[0]);
            int value = atoi(tokens[1]);
            int *current_values = hmget(*pageOrderingRules, key);

            arrput(current_values, value);
            hmput(*pageOrderingRules, key, current_values);
        }
    }

    free(buffer);
}

void print_por(PageOrderingRules *pageOrderingRules) {
    for (int i = 0; i < hmlen(pageOrderingRules); i++) {
        int key = pageOrderingRules[i].key;
        int *value = pageOrderingRules[i].value;
        printf("%d: ", key);
        print_arr(value);
        printf("\n");
    }
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
