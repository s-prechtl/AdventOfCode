#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

int count_lines(char *filename);

int check_report(char *line, int is_problem);

int main() {
    FILE *file;
    char filename[] = "input.txt";
    char *buffer = malloc(BUFFER_SIZE);
    int count = 0;
    int check;

    file = fopen(filename, "r");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    while (fgets(buffer, BUFFER_SIZE, file) != NULL) {
        char *buffer_copy = malloc(BUFFER_SIZE);
        memcpy(buffer_copy, buffer, BUFFER_SIZE);
        check = check_report(buffer, 0);
        count += check;
        if (!check) {
            memcpy(buffer, buffer_copy, BUFFER_SIZE);
            remove_second_level(buffer);
            check = check_report(buffer, 1);
            count += check;
        }
        if (!check) {
            memcpy(buffer, buffer_copy, BUFFER_SIZE);
            remove_first_level(buffer);
            check = check_report(buffer, 1);
            count += check;
        }
        if (!check) {
            printf("%s", buffer_copy);
        }
    }
    printf("%d", count);

    fclose(file);

    return 0;
}

void remove_second_level(char *report) {
    char *first_space = strchr(report, ' ');
    if (!first_space)
        return;

    char *second_space = strchr(first_space + 1, ' '); // Find the second space
    if (!second_space)
        return;

    memmove(first_space + 1, second_space + 1, strlen(second_space + 1) + 1);
}

void remove_first_level(char *report) {
    char *first_space = strchr(report, ' ');
    if (!first_space)
        return;
    memmove(report, first_space + 1, strlen(first_space + 1) + 1);
}

int check_report(char *report, int is_problem) {
    char *current_number_string;
    char *saveptr;
    int previous_level = -1;
    int is_decreasing = -1;
    int is_last = 0;
    int level;
    while ((current_number_string = strtok_r(report, " ", &saveptr))) {
        if (report) {
            report = NULL;
        }

        if (current_number_string[strlen(current_number_string) - 1] == '\n') {
            current_number_string[strlen(current_number_string) - 1] = '\0';
            is_last = 1;
        }
        level = atoi(current_number_string);
        if (previous_level == -1) {
            previous_level = level;
            continue;
        }

        if (abs(level - previous_level) < 1 || abs(level - previous_level) > 3) {
            if (!is_problem) {
                if (is_last) {
                    return 1;
                }
                is_problem = 1;
                continue;
            } else {
                break;
            }
        }

        if (is_decreasing == -1) {
            is_decreasing = (level < previous_level) ? 1 : 0;
        }
        if (is_decreasing && level < previous_level) {
            previous_level = level;
            if (is_last) {
                return 1;
            }
        } else if (!is_decreasing && level > previous_level) {
            previous_level = level;
            if (is_last) {
                return 1;
            }
        } else {
            if (!is_problem) {
                if (is_last) {
                    return 1;
                }
                is_problem = 1;
                continue;
            } else {
                break;
            }
        }
    }
    return 0;
}
