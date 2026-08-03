#twoSum problem leetcode 1
def twoSum(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
          cumsum= nums[left]+nums[right]
          if cumsum==target:
              return nums[left],nums[right]
          elif cumsum<target:
               left+=1
          elif cumsum>target:
               right-=1
    return False
print(twoSum([1, 2, 3, 4, 6],6))


