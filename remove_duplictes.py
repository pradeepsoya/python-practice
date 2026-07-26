def removeDuplicates(l):
    li=[]
    for i in l:
        if i not in li:
            li.append(i)
    return li
print(removeDuplicates([1,2,5,2,4,6,1]))
