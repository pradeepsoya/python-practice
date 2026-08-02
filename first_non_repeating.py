def nonRepeating(arr):
    for i in arr:
        count=0
        for j in arr:
            if i==j:
                count+=1
        if count==1:
            return i
    return -1
print(nonRepeating([1, 2, 1, 3, 3]))