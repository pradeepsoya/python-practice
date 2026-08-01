def rotateArrayLeft(arr):
    temp=arr[0]
    length=len(arr)
    for i in range(length-1):
        arr[i]=arr[i+1]
    arr[length]=temp
    return arr
print(rotateArrayLeft([1,2,3,4,5]))

