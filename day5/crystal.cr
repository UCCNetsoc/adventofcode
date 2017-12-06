puzzle_input = File.read("d5.in").strip.split("\n").map { |num| num.to_i }

test_input = [0, 3, 0, 1, -3]

def problem1(input)
  # Given a list of numbers, interpret them as jump instructions to move around the list
  # Increment each instruction when you use it, and return the number of steps taken to leave the list
  steps = 0
  index = 0
  length = input.size
  while index >= 0 && index < length
    jump = input[index]
    input[index] += 1
    index += jump
    steps += 1
  end
  steps
end

puts problem1 test_input.clone # Should be 5
puts problem1 puzzle_input.clone

def problem2(input)
  # Pretty much the same as before but if the jump instruction is >= 3 you decrement instead of increment
  steps = 0
  index = 0
  length = input.size
  while index >= 0 && index < length
    jump = input[index]
    if jump < 3
      input[index] += 1
    else
      input[index] -= 1
    end
    index += jump
    steps += 1
  end
  steps
end

puts problem2 test_input.clone # Should be 10
puts problem2 puzzle_input.clone
