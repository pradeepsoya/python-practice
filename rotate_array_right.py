def rotateArrayRight(arr):
    length=len(arr)
    temp=arr[length-1]
    for i in range(length-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    return arr
print(rotateArrayRight([1,3,2,4,9]))