#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int get_max_line_length(char *filename);
int *get_numbers_from_mul(const char *s, int start, int end);
void init_regex(regex_t *regex, char *patter);

int main(void) {
    regex_t mul_regex;
    regex_t do_regex;
    regex_t dont_regex;
    int reti;

    int do_start, dont_start = -1;
    char msgbuf[100];
    FILE *file;
    char filename[] = "input.txt";
    const int MAX_LINE_LENGTH = get_max_line_length(filename);
    char *buffer = malloc(MAX_LINE_LENGTH * sizeof(char));
    int sum = 0;
    int is_enabled = 1;
    regmatch_t match[1];
    regmatch_t do_dont_match[1];

    file = fopen(filename, "r");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    init_regex(&mul_regex, "mul\\([0-9]{1,3},[0-9]{1,3}\\)");
    init_regex(&do_regex, "do\\(\\)");
    init_regex(&dont_regex, "don't\\(\\)");

    while (fgets(buffer, MAX_LINE_LENGTH, file) != NULL) {
        const char *search_start = buffer;
        while ((reti = regexec(&mul_regex, search_start, 1, match, 0)) == 0) {
            int match_start = match[0].rm_so;
            int match_end = match[0].rm_eo;

            reti = regexec(&do_regex, search_start, 1, do_dont_match, 0);
            if (!reti) {
                do_start = do_dont_match[0].rm_so;
            } else {
                do_start = strlen(search_start);
            }

            reti = regexec(&dont_regex, search_start, 1, do_dont_match, 0);
            if (!reti) {
                dont_start = do_dont_match[0].rm_so;
            }

            if (do_start < match_start && (dont_start > match_start || dont_start < do_start)) {
                is_enabled = 1;
            }

            if (dont_start < match_start && (do_start > match_start || do_start < dont_start)) {
                is_enabled = 0;
            }

            if (is_enabled) {
                int *numbers = get_numbers_from_mul(search_start, match_start, match_end);

                sum += numbers[0] * numbers[1];

                free(numbers);
            }

            if (is_enabled) {
                search_start += match_end;
            } else {
                if (do_start == 0) {
                    do_start = 1;
                }
                search_start += do_start;
            }
        }
    }

    printf("%d\n", sum);

    fclose(file);
    regfree(&mul_regex);
    return 0;
}

int get_max_line_length(char *filename) {
    FILE *file = fopen(filename, "r");

    if (file == NULL) {
        perror("Error opening file");
        return -1;
    }

    int CUR_MAX = 4095;
    char *buffer = (char *)malloc(sizeof(char) * CUR_MAX);
    int length = 0;
    char ch = ' ';

    while ((ch != '\n') && (ch != EOF)) {
        if (length == CUR_MAX) {
            CUR_MAX *= 2;
            buffer = realloc(buffer, CUR_MAX);
        }
        ch = getc(file);
        buffer[length] = ch;
        length++;
    }

    free(buffer);
    fclose(file);
    return CUR_MAX;
}

void init_regex(regex_t *regex, char *pattern) {
    int reti = regcomp(regex, pattern, REG_EXTENDED);
    if (reti) {
        fprintf(stderr, "Could not compile regex\n");
        exit(1);
    }
}

int *get_numbers_from_mul(const char *s, int start, int end) {
    char *num1 = malloc(3);
    char *num2 = malloc(3);
    int *numbers = malloc(2 * sizeof(int));

    int is_first = 1;
    int current_number_index = 0;
    for (int i = start; i < end; i++) {
        char current = s[i];
        if (current >= '0' && current <= '9') {
            if (is_first) {
                num1[current_number_index] = current;
                current_number_index++;
            } else {
                num2[current_number_index] = current;
                current_number_index++;
            }
        } else if (current == ',') {
            is_first ^= 1;
            current_number_index = 0;
        }
    }

    numbers[0] = atoi(num1);
    numbers[1] = atoi(num2);
    free(num1);
    free(num2);

    return numbers;
}
