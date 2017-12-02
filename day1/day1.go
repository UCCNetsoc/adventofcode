package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func day1(num string) int {
	sum := 0
	for i, curr := range num {
		if curr == rune(num[(i+1)%len(num)]) {
			n, err := strconv.Atoi(string(curr))
			if err != nil {
				panic(err)
			}
			sum += n
		}
	}
	return sum
}

func main() {
	f, err := os.Open(os.Args[1])
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		l := scanner.Text()
		fmt.Println(day1(l))
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
