puzzle_input = 277678

test_cases_1 = [
  [1, 0],
  [12, 3],
  [23, 2],
  [1024, 31],
]

def find_size(input)
  # Given a number, find the smallest n where n is odd and n^2 is >= input
  n = 1
  until n.abs2 >= input
    n += 2
  end
  n
end

def manhattan_distance(source, destination)
  # Get the manhattan distance between source and destination
  source[0] = 0 if source[0] < 0
  source[1] = 0 if source[1] < 0
  return (source[0] - destination[0]).abs + (source[1] - destination[1]).abs
end

def problem1(input)
  # Find the smallest n where n is odd and n^2 is > input
  n = find_size input
  # After finding the size of our m x m matrix, we need to find the coords of our input
  destination = (n - 1) / 2
  # Find position of my input
  # Input must reside in between the [n-2][n-2] and [n-1][n-1]
  # Starting from [n-2][n-2], go right 1, up (n-2), left (n-2) + 1, down (n-2) + 1 and right (n-2) + 1
  coords = [n - 2, n - 2]
  value = (n - 2).abs2
  # Check initial value
  if value == input
    return manhattan_distance(coords, [destination, destination])
  end
  changes = [1, n - 2, (n - 2) + 1, (n - 2) + 1, (n - 2) + 1]
  procs = [
    # Go right one
    ->(coords : Array(Int32)) { coords[1] += 1 },
    # Go up (n-2)
    ->(coords : Array(Int32)) { coords[0] -= 1 },
    # Go left (n-2) + 1
    ->(coords : Array(Int32)) { coords[1] -= 1 },
    # Go down (n-2) + 1
    ->(coords : Array(Int32)) { coords[0] += 1 },
    # Go right (n-2) + 1
    ->(coords : Array(Int32)) { coords[1] += 1 },
  ]
  changes.each.with_index do |change, i|
    (0...change).each do |_|
      value += 1
      procs[i].call coords
      if value == input
        return manhattan_distance(coords, [destination, destination])
      end
    end
  end
end

test_cases_1.each do |cse|
  puts "Testing problem1(#{cse[0]}) == #{cse[1]} -> #{problem1(cse[0]) == cse[1]} (#{problem1(cse[0])})"
end
puts problem1 277678

def get_sum(matrix, row, col)
  # Returns the sum of all values around a position in a matrix
  max = matrix.size - 1
  positions = [
    [row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
    [row, col - 1], [row, col + 1],
    [row + 1, col - 1], [row + 1, col], [row + 1, col + 1],
  ]
  sum = 0
  positions.each do |position|
    row_pos, col_pos = position[0].clamp(0, max), position[1].clamp(0, max)
    sum += matrix[row_pos][col_pos]
  end
  sum
end

def print_matrix(matrix)
  matrix.each do |row|
    puts row
  end
  puts "\n"
end

def problem2(input)
  # Continuing with the spiral memory pattern, find the first cell larger than your input
  # As much overkill as it is, we should still be safe to use n like last time
  n = find_size input
  matrix = [] of Array(Int32)
  (0...n).each do |_|
    matrix << Array.new(n, 0)
  end
  x, y = [(n - 1) / 2, (n - 1) / 2]
  # Format is matrix[y][x]
  matrix[y][x] = 1
  x += 1
  distance = 1
  while true
    # Fill current box and `dist` boxes above (-y)
    (y - distance..y).reverse_each do |j|
      new_num = get_sum(matrix, j, x)
      if new_num > input
        return new_num
      end
      matrix[j][x] = new_num
    end
    # Calculate the final point of y
    y -= distance
    # Increase distance here again
    distance += 1

    # Fill left (-x)
    (x - distance..x).reverse_each do |i|
      new_num = get_sum(matrix, y, i)
      if new_num > input
        return new_num
      end
      matrix[y][i] = new_num
    end
    # Calculate the final point of x
    x -= distance

    # Fill current box and `dist` boxes below (+y)
    (y..y + distance).each do |j|
      new_num = get_sum(matrix, j, x)
      if new_num > input
        return new_num
      end
      matrix[j][x] = new_num
    end
    # Calculate the final point of y
    y += distance

    # Increase distance here
    distance += 1
    # Fill Right (+x)
    (x..x + distance).each do |i|
      new_num = get_sum(matrix, y, i)
      if new_num > input
        return new_num
      end
      matrix[y][i] = new_num
    end
    # Calculate the final point of x
    x += distance
  end
end

puts problem2 puzzle_input
