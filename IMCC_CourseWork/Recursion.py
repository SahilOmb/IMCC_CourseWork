def num(n):
    print(n)
    if n > 0:       # Changed to > 0 to stop after printing 0
        num(n - 1)  # Call the function 'num', not the variable 'n'

num(5)
