puzzle_input = File.read "d2.in"

def problem1(input)
  # Calculate difference between max and min of each row and get total sum
  rows = input.split "\n"
  sum = 0
  rows.each do |row|
    nums = row.split("\t").map { |n| n.to_i }
    sum += (nums.max - nums.min)
  end
  sum
end

puts problem1 puzzle_input

def problem2(input)
  rows = input.split "\n"
  sum = 0
  rows.each do |row|
    # Now we need to find the two numbers that divide evenly and get the sum of the result of that division
    nums = row.split("\t").map { |n| n.to_i }
    nums.each do |num|
      nums.each do |other|
        if other <= num / 2 && num % other == 0
          sum += num / other
          break
        end
      end
    end
  end
  sum
end

puts problem2 puzzle_input
