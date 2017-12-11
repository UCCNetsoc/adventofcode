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
			s                    = stack.New()
			groups, garbage      int
			cancelled, isGarbage bool
		)
		for _, r := range sc.Text() {
			if cancelled {
				cancelled = false
				continue
			}

			switch r {
			case '!':
				cancelled = true
			case '<':
				if isGarbage {
					garbage++
				}
				isGarbage = true
			case '>':
				isGarbage = false
			case '{':
				if isGarbage {
					garbage++
					continue
				}
				s.Push(r)
			case '}':
				if isGarbage {
					garbage++
					continue
				}
				groups += s.Len()
				if _, err := s.Pop(); err != nil {
					panic(err)
				}
			default:
				if isGarbage {
					garbage++
				}
			}
		}
		fmt.Println(groups, garbage)
	}

	if err := sc.Err(); err != nil {
		panic(err)
	}
}
