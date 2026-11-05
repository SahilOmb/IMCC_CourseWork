'''
#list
fruits = ["apple","orange","banana","coconut"]
print(fruits[::-1])
print(len(fruits))
print("apple" in fruits)
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(3,"cherry")
fruits.sort()
print(fruits)
print(fruits.count("banana"))
for fruit in fruits:
  print(fruit)
'''
'''
#set
fruits = {"apple","orange","banana","coconut","apple"}
print(len(fruits))
fruits.add("pizza")
fruits.remove("pizza")
fruits.pop()
print(fruits)
 '''

#tuple
fruits = ("apple","orange","banana","coconut")
print(len(fruits))
print("pineapple" in fruits)
print(fruits.index("apple"))
print(fruits.count("apple"))