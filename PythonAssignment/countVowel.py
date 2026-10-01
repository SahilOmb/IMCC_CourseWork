text = input("enter a number :")
count=0

for char in text:
    if char in "aeiouAEIOU":
        count+=1
print(count)