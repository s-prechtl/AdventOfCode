#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

int count_lines(char *filename);
int compare_ints(const void *a, const void *b);

int main() {
  FILE *file;
  char filename[] = "input.txt";
  char *buffer = malloc(BUFFER_SIZE);
  char *saveptr;
  char *current_number_string;
  const int lines = count_lines(filename);
  int *first_numbers = malloc(lines * sizeof(int));
  int *second_numbers = malloc(lines * sizeof(int));
  int current_position = 0;
  int sum = 0;

  file = fopen(filename, "r");

  if (file == NULL) {
    perror("Error opening file");
    return 1;
  }

  while (fgets(buffer, BUFFER_SIZE, file) != NULL) {
    char *line = buffer;
    int is_first = 1;
    while ((current_number_string = strtok_r(line, "   ", &saveptr))) {
      if (current_number_string[strlen(current_number_string) - 1] == '\n') {
        current_number_string[strlen(current_number_string) - 1] = '\0';
      }
      if (is_first) {
	first_numbers[current_position] = atoi(current_number_string);
      } else {
	second_numbers[current_position] = atoi(current_number_string);
      }
      is_first ^= 1;
      if (line) {
        line = NULL;
      }
    }
    current_position++;
  }
  qsort(first_numbers, lines, sizeof(int), compare_ints);
  qsort(second_numbers, lines, sizeof(int), compare_ints);
  
  for (int i = 0; i < lines; i++) {
	int difference = abs(first_numbers[i] - second_numbers[i]);
	sum += difference;
  }

  printf("%d\n", sum);
  fclose(file);

  return 0;
}

int count_lines(char *filename) {
  char c;
  int lines = 0;
  FILE *file = fopen(filename, "r");

  if (!file) {
    return 0;
  }

  while (!feof(file)) {
    c = fgetc(file);
    if (c == '\n') {
      lines++;
    }
  }

  fclose(file);
  return lines;
}

int compare_ints(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}
