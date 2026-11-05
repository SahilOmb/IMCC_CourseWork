import os


with open("example.txt",'w') as file:
    file.write("hwllo world")

with open("example.txt", 'a') as file:
    file.write("\n this is the line2")

with open("example.txt","r") as file:
    content = file.read()
    print(content)
