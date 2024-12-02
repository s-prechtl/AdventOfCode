#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

int count_lines(char *filename);

int main() {
    FILE *file;
    char filename[] = "input.txt";
    char *buffer = malloc(BUFFER_SIZE);
    char *saveptr;
    char *current_number_string;
    int count = 0;

    file = fopen(filename, "r");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    while (fgets(buffer, BUFFER_SIZE, file) != NULL) {
        char *line = buffer;
        int previous_level = -1;
        int is_decreasing = -1;
        int is_last = 0;
        while ((current_number_string = strtok_r(line, " ", &saveptr))) {
            if (line) {
                line = NULL;
            }
            if (current_number_string[strlen(current_number_string) - 1] == '\n') {
                current_number_string[strlen(current_number_string) - 1] = '\0';
                is_last = 1;
            }
            int level = atoi(current_number_string);
            if (previous_level == -1) {
                previous_level = level;
                continue;
            }

            if (abs(level - previous_level) < 1 || abs(level - previous_level) > 3) {
                break;
            }

            if (is_decreasing == -1) {
                is_decreasing = (level < previous_level) ? 1 : 0;
            }
            if (is_decreasing && level < previous_level) {
		previous_level = level;
                if (is_last) {
                    count++;
                }
            } else if (!is_decreasing && level > previous_level) {
		previous_level = level;
                if (is_last) {
                    count++;
                }
            } else {
                break;
            }
        }
    }
    printf("%d", count);

    fclose(file);

    return 0;
}
