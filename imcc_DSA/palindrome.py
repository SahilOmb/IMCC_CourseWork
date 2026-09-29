
original_num = 125
num = original_num
reversed_num = 0
while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10

if original_num == reversed_num:
    print( "is a palindrome number.")
else:
    print("its not")