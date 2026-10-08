print("first")
count = 0
while count < 5:
    print(count)   # Printed first if you want matching output to the for loop
    count += 1 
print("second")
for i in range(5):
    print(i)
print("third")
for i in range(4):
    if i== 3:
        print(i)
        continue
