def sortArray(arr1, arr2):
    temp = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i += 1
        else:
            temp.append(arr2[j])
            j += 1
    while i < len(arr1):
        temp.append(arr1[i])
        i += 1
    while j < len(arr2):
        temp.append(arr2[j])
        j += 1

    return temp

print(sortArray([1, 2, 3], [4, 5, 6]))