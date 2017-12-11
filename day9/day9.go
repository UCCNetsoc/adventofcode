package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/adamgillessen/go/stack"
)

func main() {
	f, err := os.Open("d9.in")
	if err != nil {
		panic(err)
	}

	sc := bufio.NewScanner(f)
	sc.Buffer([]byte{}, 1024*1024*1024)

	for sc.Scan() {
		var (
			s                 = stack.New()
			groups            int
			skipNext, garbage bool
		)
		for _, r := range sc.Text() {
			if skipNext {
				skipNext = false
				continue
			}

			switch r {
			case '!':
				skipNext = true
			case '<':
				garbage = true
			case '>':
				garbage = false
			case '{':
				if garbage {
					continue
				}
				s.Push(r)
			case '}':
				if garbage {
					continue
				}
				groups += s.Len()
				if _, err := s.Pop(); err != nil {
					panic(err)
				}
			}
		}
		fmt.Println(groups)
	}

	if err := sc.Err(); err != nil {
		panic(err)
	}
}
