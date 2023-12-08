package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const MAX_RED = 12
const MAX_GREEN = 13
const MAX_BLUE = 14


func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	games := strings.Split(string(content), "\n")
    sum_of_possibles := 0

    for _, game := range games {
        possible := true
        game_info := strings.Split(strings.Replace(game, "Game ", "", 1), ":")
        gameId, err := strconv.Atoi(game_info[0])
        if err != nil {
            continue
        }
        var cubes []string
        temp := strings.Split(game_info[1], ", ")
        for _, tempSplit := range temp {
           cubes = append(cubes, strings.Split(tempSplit, "; ")...)
        }


        for _, cube := range cubes {
            amount, err := strconv.Atoi(strings.Split(strings.TrimSpace(cube), " ")[0])
            if err != nil {
                fmt.Println(cube, "heast")
                continue
            }

            color := strings.Split(cube, " ")[1]

            if color == "green" && amount > MAX_GREEN {
                possible = false
            } else if color == "red" && amount > MAX_RED {
                possible = false
            } else if amount > MAX_BLUE {
                possible = false
            }
        }

        if possible == true {
            sum_of_possibles += gameId
        }
    }

    fmt.Println(sum_of_possibles)

}
