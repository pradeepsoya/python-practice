def arraySorted(arr):
    if len(arr)==0 or len(arr)==1:
        return True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
           return False
    return True
print(arraySorted([1,2,3,4]))