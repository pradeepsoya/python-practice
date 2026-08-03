def removeElement(arr, val):
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != val:
            arr[slow] = arr[fast]
            slow += 1

    return arr[:slow]


print(removeElement([3, 2, 2, 3], 3))