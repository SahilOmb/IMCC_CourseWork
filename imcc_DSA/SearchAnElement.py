n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

search_element = int(input())

if search_element in array:
    position = array.index(search_element) + 1
    print(f"Number found at position {position}")
else:
    print("Number not found")
