package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func part1(num string) int {
	sum := 0
	for i := range num {
		if num[i] == num[(i+1)%len(num)] {
			n, err := strconv.Atoi(string(num[i]))
			if err != nil {
				panic(err)
			}
			sum += n
		}
	}
	return sum
}

func part2(num string) int {
	sum := 0
	offset := len(num) / 2
	for i := range num {
		if num[i] == num[(i+offset)%len(num)] {
			n, err := strconv.Atoi(string(num[i]))
			if err != nil {
				panic(err)
			}
			sum += n
		}
	}
	return sum
}

func main() {
	f, err := os.Open("d1.in")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		l := scanner.Text()
		fmt.Println(part1(l))
		fmt.Println(part2(l))
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
