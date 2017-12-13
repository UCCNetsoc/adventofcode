package main

import (
	"bytes"
	"encoding/hex"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const knotlen = 256

func reverse(a *[knotlen]uint, c, l int) {
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

func part1() {
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

	a := &[knotlen]uint{}
	for i := 0; i < knotlen; i++ {
		a[i] = uint(i)
	}

	var skipSize, current int
	for _, l := range lengths {
		reverse(a, current, l)
		current = (current + l + skipSize) % knotlen
		skipSize++
	}
	fmt.Println("Part1:", a[0]*a[1])
}

func xor16(a *[knotlen]uint, start, end int) byte {
	var block uint
	for i := start; i < end; i++ {
		block = block ^ a[i]
	}
	return byte(block)

}

func part2() {
	lengthFile, err := ioutil.ReadFile("d10.in")
	if err != nil {
		panic(err)
	}

	var lengths []int
	for _, l := range bytes.Trim(lengthFile, "\n") {
		lengths = append(lengths, int(l))
	}

	lengths = append(lengths, []int{17, 31, 73, 47, 23}...)

	a := &[knotlen]uint{}
	for i := 0; i < knotlen; i++ {
		a[i] = uint(i)
	}

	var skipSize, current int

	for round := 0; round < 64; round++ {
		for _, l := range lengths {
			reverse(a, current, l)
			current = (current + l + skipSize) % knotlen
			skipSize++
		}
	}

	var denseHash []byte
	for block := 0; block < knotlen; block += 16 {
		denseHash = append(denseHash, xor16(a, block, block+16))
	}

	hexString := make([]byte, hex.EncodedLen(len(denseHash)))
	hex.Encode(hexString, denseHash)

	fmt.Println("Part2:", string(hexString))
}

func main() {
	part1()
	part2()
}
