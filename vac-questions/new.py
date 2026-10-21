def countFreq(n, k):
    freq = [0] * 10
    
    while(n != 0):
        last_digit = n % 10
        freq[last_digit] += 1
        n //= 10
        
    res = []
    
    for digit, count in enumerate(freq):
        if count >= k:
            res.append(digit)
            
    return res
    
n = 13464987139

res = countFreq(n, 2)
print(res)