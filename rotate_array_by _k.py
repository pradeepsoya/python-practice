def leftRotateK(arr, k):
    n = len(arr)

    if n == 0:
        return arr

    k = k % n
    temp = []
    for i in range(k):
        temp.append(arr[i])
    for i in range(n - k):
        arr[i] = arr[i + k]
    j = 0
    for i in range(n - k, n):
        arr[i] = temp[j]
        j += 1

    return arr

print(leftRotateK([1, 2, 3, 4, 5, 6], 2))