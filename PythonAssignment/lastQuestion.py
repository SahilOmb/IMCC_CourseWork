#Read a file, split its content into words, and store them in a list.
#Print the total number of words. Print all unique words.
file = open("sample.txt", "r")
content = file.read()
file.close()

file_words = content.split()
print("Total number of words:", len(file_words))

unique_words = []

for word in file_words:
    if word not in unique_words:
        unique_words.append(word)

print("Unique words:", unique_words)
