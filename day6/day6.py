def part1():
    with open("d6.in") as f:
        mem = list(map(int, f.read().strip().split()))
    
    seen_configs = set()
    redistributions = 0
    while True:
        redistributions += 1
        seen_configs.add(hash(tuple(mem)))

        max_n, max_i = float("-inf"), -1
        for i, n in enumerate(mem):
            if n > max_n:
                max_n = n
                max_i = i

        to_alloc = mem[max_i]
        mem[max_i] = 0
        inc = lambda i: (i+1)%len(mem)
        i = inc(max_i)
        while to_alloc > 0:
            mem[i] += 1
            to_alloc -= 1
            i = inc(i)

        if hash(tuple(mem)) in seen_configs:
            break
    print(redistributions)


def part2():
    with open("d6.in") as f:
        mem = list(map(int, f.read().strip().split()))
    
    seen_configs = {}
    redistributions = 0
    while True:
        seen_configs[hash(tuple(mem))] = redistributions

        max_n, max_i = float("-inf"), -1
        for i, n in enumerate(mem):
            if n > max_n:
                max_n = n
                max_i = i

        to_alloc = mem[max_i]
        mem[max_i] = 0
        inc = lambda i: (i+1)%len(mem)
        i = inc(max_i)
        while to_alloc > 0:
            mem[i] += 1
            to_alloc -= 1
            i = inc(i)
        redistributions += 1

        if hash(tuple(mem)) in seen_configs:
            break
    print(redistributions - seen_configs[hash(tuple(mem))])


if __name__ == "__main__":
    part1()
    part2()