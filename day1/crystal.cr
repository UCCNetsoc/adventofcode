def problem1(number)
  s = number.to_s
  sum = 0
  # Find all the numbers where it is equal to the number previous
  s.each_char.with_index do |c, i|
    if s[i - 1] == c
      sum += c.to_i
    end
  end
  sum
end

def problem2(number)
  s = number.to_s
  sum = 0
  # Now checking half way around the cyclic list
  s.each_char.with_index do |c, i|
    index = (i + (s.size / 2)) % s.size
    if s[index] == c
      sum += c.to_i
    end
  end
  sum
end
