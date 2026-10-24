
name = input("enter your name:")

while name =="":
    print("you didnt enter your name ?")
    name = input("enter your name:")
print(f"hell0 {name}")

food = input("enter your fav food")

while food !='q':
    print(f"you like {food}")
    food = input("enter your fav food (q to quit)")
print("bye bye" )


num = 1

while num <10:
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1

while True:
    num = int(input("enter a positive num to exit the loop "))
    if num > 0 :
        break