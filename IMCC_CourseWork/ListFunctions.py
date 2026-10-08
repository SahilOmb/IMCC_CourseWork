my_list=[]
print(my_list)

fruits=['apple','banana','mango']
print(fruits)

nums=[10,20,30,40]
print(nums[0],nums[-2])

fruits.append("guava")
print(fruits)

fruits.insert(2,"grapes")
print(fruits)

fruits.remove("banana")
print(fruits)

Last_fruit=fruits.pop()
print(Last_fruit)


print("number of items", len(fruits))

print(sum(nums))
print(sorted(nums,reverse=True))


#create a list of 10 nums print the sum of last 4 elements of the list 
#find diff bettwen max and min element of the list 
#insert a number at 6th position , this number must be 1/3 of number stored at 4th position 
#