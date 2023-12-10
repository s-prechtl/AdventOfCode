package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func is_adjacent_to_symbol(y int, x int, lines []string) bool {
	for i := y - 1; i <= y+1; i++ {
		for j := x - 1; j <= x+1; j++ {
			if i < 0 || j < 0 || i >= len(lines) || j >= len(lines[i]) {
				continue
			}

			_, error := strconv.Atoi(string(lines[i][j]))
			if error == nil {
				continue
			}

			if lines[i][j] != '.' {
				return true
			}
		}
	}
	return false
}

func print_number_with_surronding(number string, y int, end_x int, lines []string) {
	x := end_x - len(number) + 1
	for i := y - 1; i <= y+1; i++ {
		for j := x - 1; j <= end_x+1; j++ {
			if i < 0 || j < 0 || i >= len(lines) || j >= len(lines[i]) {
				continue
			}

			fmt.Print(string(lines[i][j]))
		}
		fmt.Println()
	}
	fmt.Println()
	fmt.Println()
}

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(content), "\n")
	sum_of_parts := 0

	for y, line := range lines {
		current_number_string := ""
		current_number_is_vald := false
		for x, char := range line {
			_, err := strconv.Atoi(string(char))
			if err != nil {
				if current_number_string != "" {
					number, error := strconv.Atoi(current_number_string)
					if error != nil {
						fmt.Println("Error converting string to int")
					}

					if current_number_is_vald {
						sum_of_parts += number
                    }

					current_number_string = ""

				}
				current_number_is_vald = false
				continue
			}
			current_number_string += string(char)

			if !current_number_is_vald && is_adjacent_to_symbol(y, x, lines) {
				current_number_is_vald = true
			}
		}
	}

	fmt.Println(sum_of_parts)
}
