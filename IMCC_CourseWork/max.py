def get_max(*num):
    if len(num) ==0:
        return None
    max_num = num[0]
    for n in num:
        if n > max_num:
            max_num = n
    return max_num

print(get_max(3,12,56,78,1,45))
print(get_max('arushi','mahi','vibhavi'))