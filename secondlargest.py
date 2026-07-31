#find the second largest element in a list
def secondlargest(nums):
    largest=0
    secondlargest=0
    for i in nums:
        if i>largest :
            secondlargest=largest
            largest=i
        elif largest>i>secondlargest:
            secondlargest=i
    return secondlargest   
print(secondlargest([10,10, 8, 9]))