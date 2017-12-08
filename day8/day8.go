package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	inFile = "d8.in"
)

func main() {
	f, err := os.Open(inFile)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	var (
		sc        = bufio.NewScanner(f)
		registers = make(map[string]int)
		maxVal    int
	)
	for sc.Scan() {
		var (
			reg  string
			op   string
			n    int
			cReg string
			cOp  string
			cN   int
		)
		if _, err := fmt.Sscanf(sc.Text(), "%s %s %d if %s %s %d", &reg,
			&op, &n, &cReg, &cOp, &cN); err != nil {
			panic(err)
		}

		if _, ok := registers[reg]; !ok {
			registers[reg] = 0
		}
		if _, ok := registers[cReg]; !ok {
			registers[cReg] = 0
		}

		var (
			crValue = registers[cReg]
			cond    bool
		)
		switch cOp {
		case "<":
			cond = crValue < cN
		case "<=":
			cond = crValue <= cN
		case ">":
			cond = crValue > cN
		case ">=":
			cond = crValue >= cN
		case "==":
			cond = crValue == cN
		case "!=":
			cond = crValue != cN
		}

		if cond {
			var newN int
			switch op {
			case "inc":
				newN = registers[reg] + n
			case "dec":
				newN = registers[reg] - n
			}
			registers[reg] = newN

			if newN > maxVal {
				maxVal = newN
			}
		}
	}

	if err := sc.Err(); err != nil {
		panic(err)
	}

	maxEndVal := math.MinInt64
	for _, n := range registers {
		if n > maxEndVal {
			maxEndVal = n
		}
	}
	fmt.Println("Part1:", maxEndVal)
	fmt.Println("Part2:", maxVal)
}
