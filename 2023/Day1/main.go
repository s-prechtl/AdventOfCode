package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)


func findFirstNumberInString(input string) string {
    for _, c := range input {
        if string(c) >= "0" && string(c) <= "9" {
            return string(c)
        }
    }
    return ""
}

func numbersMap() map[string]string {
    return map[string]string{
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
}

func findFirstNumberIncludingSpelledOutNumbers(input string) (result string) {
    numbers := numbersMap()
    spelledIndex := int(^uint(0) >> 1)
    for spelled, number := range numbers {
        i := strings.Index(input, spelled)
        if i != -1 && i < spelledIndex {
            result = number
            spelledIndex = i
        }
    }

    for i, c := range input {
        if string(c) >= "0" && string(c) <= "9" {
            if i < spelledIndex {
                return string(c)
            } else {
                return result
            }
        }
    }
    return result
}

func findFirstNumberIncludingSpelledOutNumbersReversedOrder(input string) (result string) {
    numbers := numbersMap()
    spelledIndex := -1
    for spelled, number := range numbers {
        i := strings.LastIndex(input, spelled)
        if i != -1 && i > spelledIndex {
            result = number
            spelledIndex = i
        }
    }

    for i, c := range input {
        if string(c) >= "0" && string(c) <= "9" && i > spelledIndex{
            spelledIndex = i
            result = string(c)
        }
    }
    return result
}

func reverse(input string) (result string) {
    for _, c := range input {
        result = string(c) + result
    }
    return result
}

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(content), "\n")
	sum := 0

	for _, line := range lines {
        if (line == "") {
            continue
        }
        // Day 1
        // value := findFirstNumberInString(line)
        // value += findFirstNumberInString(reverse(line))

        // Day 2
		value := findFirstNumberIncludingSpelledOutNumbers(line)
        value += findFirstNumberIncludingSpelledOutNumbersReversedOrder(line)
        fmt.Println(line, value)
        if len(value) != 2 {
            fmt.Println("Number couldn't be found" + line)
        }
		number, err := strconv.Atoi(value)
		if err != nil {
			fmt.Println("Number couldn't be converted" + value)
		}
		sum += number
	}
    fmt.Println(sum)
}
