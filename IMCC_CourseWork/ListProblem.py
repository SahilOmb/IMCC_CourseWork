#create a list of number and string accept the values from users, seperate the list from the max number then display in desc order
user_input = input("Enter numbers and words: ")
items = user_input.split()

numbers = []
strings = []

for item in items:
    if item.isdigit():
        numbers.append(int(item))  # Put numbers here
    else:
        strings.append(item)
biggest_num = max(numbers)
numbers.remove(biggest_num)

# 4. Sort backwards (Descending)
numbers.sort(reverse=True)
strings.sort(reverse=True)

# 5. Show the results
print("Highest Number:", biggest_num)
print("Other Numbers (High to Low):", numbers)
print("Words (Z to A):", strings)