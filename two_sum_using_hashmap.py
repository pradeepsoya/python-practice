def twoSumHashMap(nums, target):
    hash_map={}
    complement=0
    for i,value in enumerate(nums):
        complement=target-value
        if complement in hash_map:
            return (hash_map[complement],i)
        hash_map[value]=i
    return -1
print(twoSumHashMap([1, 2, 3, 4, 6], 6))