num=int(input("enter a number"))
p = len(str(num))
n = num
sum =0
while(num>0):
    sum+=(num%10)**p
    num//=10
if(n==sum):
    print("nunnber is armstong")
else:
    print("its not")
