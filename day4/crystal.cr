puzzle_input = File.read("d4.in").strip

def problem1(input)
  # Split the input into passphrases
  phrases = input.split "\n"
  sum = 0
  # Loop through and ensure each word in the phrase is unique
  phrases.each do |phrase|
    ans = 1
    words = phrase.split
    words.each do |word|
      if words.count(word) != 1
        ans = 0
        break
      end
    end
    sum += ans
  end
  sum
end

test_input_1 = "aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa"

# Should be 2
puts problem1 test_input_1
puts problem1 puzzle_input

def problem2(input)
  # Split the input into passphrases
  phrases = input.split "\n"
  sum = 0
  # Loop through and ensure each word in the phrase is anagrammatically unique
  phrases.each do |phrase|
    ans = 1
    words = phrase.split
    words.each_combination(2) do |comb|
      word1, word2 = comb
      if word1.split(/([a-z])/).sort == word2.split(/([a-z])/).sort
        ans = 0
        break
      end
    end
    sum += ans
  end
  sum
end

test_input_2 = "abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio"

# Should be 3
puts problem2 test_input_2
puts problem2 puzzle_input
