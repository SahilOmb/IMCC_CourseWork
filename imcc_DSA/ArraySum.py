#1. Calculate Array Sum: Write a program to accept N integers into an array and calculate and display the sum of all the elements. 

n = int(input("enter a number of element "))

numbers = []
tot_sum = 0  

for i in range(n):
    num = int(input(f"Enter element {i+1}: ")) 
    tot_sum = tot_sum + num

print("Sum of all elements:", tot_sum)
