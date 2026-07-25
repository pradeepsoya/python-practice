#twoSum problem leetcode 1
def twoSum(nums,target):
    dict={}
    complement=0
    for i,value in enumerate(nums):
        complement=target-value
        if complement in dict:
            return (dict[complement],i)
        dict[value]=i
print(twoSum([2,6,5,4,7],9))
