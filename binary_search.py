def binarySearch(l, item):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==item:
           return mid
        elif item>l[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

print(binarySearch([1,2,4,7,8,9],4))
         
