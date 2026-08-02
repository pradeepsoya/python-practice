#find the first duplicate
def firstDuplicate(arr):
    temp=[]
    for i in arr:
        if i not in temp:
            temp.append(i)
        else:
            return i
    return False
print(firstDuplicate([1, 4, 2, 5, 2, 3]))