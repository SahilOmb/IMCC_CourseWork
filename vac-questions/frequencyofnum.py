n = 12495820424002

def countfreq(num):
    freq = [0] * 10
    
    while num != 0:
        lastdigi = num % 10
        freq[lastdigi] += 1
        num //= 10
        
    return freq

res = countfreq(n)

for i in range(len(res)):
    print(f"{i} -> {res[i]}")
