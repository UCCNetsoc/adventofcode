from math import sqrt, ceil

def part1():
    with open("d3.in") as f:
        n = int(f.readline().strip())
        # get the ceiling of the square-root of the number
        # if the number is even, add 1. Otherwise, it's fine.
        # This is effectivley rounding the square-root of the
        # number up to the nearest odd number.
        gamma = ceil(sqrt(n)) + int(ceil(sqrt(n))%2 == 0)

        side_distances = list(range(gamma-1, gamma//2 -1, -1)) + \
                                list(range(gamma//2 + 1, gamma-1))
        
        # we then apply the following formula to 'step back' through
        # the side distances we generated to find out where along the
        # side the given number lies.
        i = ((gamma**2) - n)%(gamma-1)
        print(side_distances[i])


if __name__ == "__main__":
    part1()