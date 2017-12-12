package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const knotlen = 256

func reverse(a *[knotlen]int, c, l int) {
	var (
		i = c
		j = (c + l - 1) % knotlen
	)
	for swap := 0; swap < l/2; swap++ {
		a[i], a[j] = a[j], a[i]
		i = (i + 1) % knotlen
		j = (j - 1 + knotlen) % knotlen
	}
}

func main() {
	lengthFile, err := ioutil.ReadFile("d10.in")
	if err != nil {
		panic(err)
	}

	var lengths []int
	for _, l := range strings.Split(strings.Trim(string(lengthFile), "\n"), ",") {
		lInt, err := strconv.Atoi(l)
		if err != nil {
			panic(err)
		}
		lengths = append(lengths, lInt)
	}

	a := &[knotlen]int{}
	for i := 0; i < knotlen; i++ {
		a[i] = i
	}

	var skipSize, current int
	for _, l := range lengths {
		reverse(a, current, l)
		current = (current + l + skipSize) % knotlen
		skipSize++
	}
	fmt.Println(a[0] * a[1])
}
