# Task 6.4

raw_word = input("Enter a word")
list_raw_word = list(raw_word)
length_raw_word = len(raw_word)
raw_word_reverse = ""
x = length_raw_word - 1


while x >= 0:
    raw_word_reverse = raw_word_reverse + list_raw_word[x]
    x = x - 1

if raw_word == raw_word_reverse:
    print("This word is a palindrome")
else:
    print("this word is not a palindrome")
    


