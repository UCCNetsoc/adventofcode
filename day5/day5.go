package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func part1() {
	f, err := os.Open("d5.in")
	if err != nil {
		panic(err)
	}

	var (
		ins []int
		sc  = bufio.NewScanner(f)
	)
	for sc.Scan() {
		offset, err := strconv.Atoi(sc.Text())
		if err != nil {
			panic(err)
		}
		ins = append(ins, offset)
	}

	var jumps, i int
	for i != len(ins) {
		off := ins[i]
		ins[i]++
		i += off
		jumps++
	}
	fmt.Println(jumps)
}

func part2() {
	f, err := os.Open("d5.in")
	if err != nil {
		panic(err)
	}

	var (
		ins []int
		sc  = bufio.NewScanner(f)
	)
	for sc.Scan() {
		offset, err := strconv.Atoi(sc.Text())
		if err != nil {
			panic(err)
		}
		ins = append(ins, offset)
	}

	var jumps, i int
	for i != len(ins) {
		off := ins[i]
		if off >= 3 {
			ins[i]--
		} else {
			ins[i]++
		}
		i += off
		jumps++
	}
	fmt.Println(jumps)
}

func main() {
	part1()
	part2()
}
