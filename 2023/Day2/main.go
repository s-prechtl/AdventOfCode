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
    sum_of_powers := 0

    for _, game := range games {
        if game == "" {
           continue
        }
        // possible := true
        min_red := 0
        min_blue := 0
        min_green := 0
        game_info := strings.Split(strings.Replace(game, "Game ", "", 1), ":")
        game_id, err := strconv.Atoi(game_info[0])
        if err != nil {
            continue
        }
        var cubes []string
        temp := strings.Split(game_info[1], ", ")
        for _, tempSplit := range temp {
           cubes = append(cubes, strings.Split(tempSplit, "; ")...)
        }


        for _, cube := range cubes {
            cube = strings.TrimSpace(cube)
            amount, err := strconv.Atoi(strings.Split(cube, " ")[0])
            if err != nil {
                fmt.Println(cube, "heast")
                continue
            }

            color := strings.Split(cube, " ")[1]

            if game_id == 3 {
                fmt.Println(cube, amount, color)
            }

            if color == "green" {
                min_green = max(amount, min_green)
            } else if color == "red" {
                min_red = max(amount, min_red)
            } else {
                min_blue = max(amount, min_blue)
            }
        }
        fmt.Println(min_red, min_green, min_blue)

        sum_of_powers += min_green * min_red * min_blue
    }

    fmt.Println(sum_of_powers)

}
