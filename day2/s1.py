from functools import reduce



def part1():
    with open("d2.in") as f:
        sheet = (map(int, l.strip().split()) for l in f)
        s = 0
        for l in sheet:
            mn, mx = reduce(lambda acc, x: (min(acc[0], x), max(acc[1], x)), l, (float("inf"), -float("inf")))
            s += mx - mn
        print(s)


def part2():
    with open("d2.in") as f:
        sheet = (list(map(int, l.strip().split())) for l in f)
        s = 0
        for l in sheet:
            for i in range(len(l)):
                for j in range(i+1, len(l)):
                    mn, mx = min(l[i], l[j]), max(l[i], l[j])
                    if mx%mn == 0:
                        s += mx/mn
                        break
        print(int(s))


if __name__ == "__main__":
    part1()
    part2()