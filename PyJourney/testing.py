'''
n = 5
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
'''
def square(n):
    return n*n
print(square(5))

def perfectno(n):
    num=n
    add=0
    for i in range(1,n):
        if n% i==0:
            add+=i
    if add == num:
        return True
    else:
        return False
print(perfectno(6))

def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(isprime(15))

def findDivisors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l
print(findDivisors(16))