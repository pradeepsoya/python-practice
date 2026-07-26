def countDigits(num):
    count=0
    while num>0:
        digit=num%10
        count+=1
        num=num//10
    return count
print(countDigits(6245))
