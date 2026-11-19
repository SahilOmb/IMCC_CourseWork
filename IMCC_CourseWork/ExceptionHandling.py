try:
    print(x)
except:
    print("error")

try:
    print(x)
except NameError:
    print("error var not defined")
except:
    print("an exception occured")

try:
    password = input("enter password :")
    if len(password) < 8:
        raise ValueError("password must be have 8 char")
    print("valid password")
except ValueError as e:
    print(e)
