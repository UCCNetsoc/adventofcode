def part1():
    with open("d5.in") as f:
        ins = [int(l.strip()) for l in f]
        ins.append(None)

        i = 0
        jumps = 0
        while ins[i] is not None:
            ins[i], i = ins[i]+1, i+ins[i]
            jumps += 1
        print(jumps)

def part2():
    with open("d5.in") as f:
        ins = [int(l.strip()) for l in f]
        ins.append(None)

        i = 0
        jumps = 0
        while ins[i] is not None:
            ins[i], i = ins[i]-1 if ins[i] >= 3 else ins[i]+1, i+ins[i]
            jumps += 1
        print(jumps)


if __name__ == "__main__":
    part1()
    part2()