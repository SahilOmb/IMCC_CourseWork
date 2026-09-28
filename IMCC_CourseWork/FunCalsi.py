
 #Simple Calculator 

def Calculator(a,b):


    print(a+b)
    print(a/b)
    print(a-b)
    print(a*b)

Calculator(7,6) 

#Advance Calculator

def Calculator(a,b):
    Choice = int(input("enter a choice"))

    match Choice:
        case 1:
            print(a+b)
        case 2:
            print(a/b)
        case 3:
            print(a-b)
        case 4:
            print(a+b)
        case _:
            print("invaild responce")

Calculator(6,5)