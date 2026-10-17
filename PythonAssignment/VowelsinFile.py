#Write a program to read a file and count how many vowels are present in its content.

file = open("sample.txt", "r")
content = file.read()
file.close()


vowels = "aeiouAEIOU"
vowel_count = 0

for char in content:
    if char in vowels:
        vowel_count = vowel_count + 1

print("Total number of voels present:", vowel_count)
