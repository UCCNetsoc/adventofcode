from math import sqrt, ceil, log10

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


class SolutionFound(Exception):
    """This exception is raised when a solution has been found."""


def part2():
    with open("d3.in") as f:
        n = int(f.readline().strip())
        
        # we will generate the square because the square will be
        # much smaller in this case. 
        # We need to figure out an upper bound on the size of the square.

        # The numbers gain an order of magnitude(ish) with each new
        # layer, so we will say that the resulting square has
        # log10(x) rounded up to number layers.
        # We then add 1 to this in case the next largest number is
        # on the next layer.
        num_layers = int(ceil(log10(n))) + 1

        # The ith layer will have side length (i*2)+1.
        side_len = (num_layers * 2) + 1
        square = [[0 for _ in range(side_len)] for _ in range(side_len)]

        def print_table():
            [print(" ".join("%2s"%e for e in row)) for row in square]

        # we then start in the middle and step through the square, generating
        # the numbers as we go.
        # When we generate a number large than the input umber, we are done.
        
        def sum_adjacent(i, j):
            s = square[i][j-1] + \
                   square[i-1][j-1] + \
                   square[i-1][j] + \
                   square[i-1][j+1] + \
                   square[i][j+1] + \
                   square[i+1][j+1] + \
                   square[i+1][j] + \
                   square[i+1][j-1]
            if s > n:
                raise SolutionFound(s)
            return s
            
        root_i, root_j = side_len//2, side_len//2
        square[root_i][root_j] = 1
        side_offset = 0
        while True:
            side_offset += 1
            try:
                # generate right side upwards
                for i in range(root_i+side_offset-1, root_i-side_offset-1, -1):
                    square[i][root_j+side_offset] = sum_adjacent(i, root_j+side_offset)
                
                # generate top side leftwards
                for j in range(root_j+side_offset, root_j-side_offset-1, -1):
                    square[root_i-side_offset][j] = sum_adjacent(root_i-side_offset, j)    
                
                # generate left side downwards
                for i in range(root_i-side_offset, root_i+side_offset+1):
                    square[i][root_j-side_offset] = sum_adjacent(i, root_j-side_offset)
                
                # generate bottom side rightwards
                for j in range(root_j-side_offset, root_j+side_offset+1):
                    square[root_i+side_offset][j] = sum_adjacent(root_i+side_offset, j)
            except SolutionFound as e:
                print(e)
                exit(0)

if __name__ == "__main__":
    part1()
    part2()