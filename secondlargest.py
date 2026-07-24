#find the second largest element in a list
def secondlargest(nums):
    second_largest=0
    largest=0
    for n in nums:
        if n>largest:
            second_largest=largest
            largest=n
        elif n>second_largest:
            second_largest=n
    return second_largest
print(secondlargest([5,2,6,9]))