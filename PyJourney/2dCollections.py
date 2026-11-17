numpad = ((1,2,3),(4,5,6),(7,8,9),('#',0,'*'))

for numbers in numpad:
    for digits in numbers:
        print(digits,end=" ")
    print()