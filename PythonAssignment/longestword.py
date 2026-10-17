#Take a sentence from the user, split it into words, and store them in a list. Print the longest word.

user_sentence = input("Enter a sentence: ")

words_list = user_sentence.split()

print("Words list:", words_list)

longest_word = ""
for word in words_list:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word is:", longest_word)
