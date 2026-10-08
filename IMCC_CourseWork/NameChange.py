name = input("Enter name :")
name=name.lower()
new_name=""

for letter in name:
    if letter in 'aeiou':
        new_name=new_name+'z'
    else:
        new_name=new_name+letter
print(new_name)

