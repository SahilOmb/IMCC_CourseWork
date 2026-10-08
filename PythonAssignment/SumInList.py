#create a list of 10 nums print the sum of last 4 elements of the list 

nums=[10,20,30,40,10,50,60,20,70,90]
print(sum(nums[-4:]))

#insert a number at 6th position , this number must be 1/3 of number stored at 4th position 
new_value=nums[3]/3

nums.insert(5,new_value)
print(nums)

