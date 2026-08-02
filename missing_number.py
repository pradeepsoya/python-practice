def missingNumber(arr,n):
    org_sum=0
    cu_sum=0
    for i in range(1,n+1):
        org_sum+=i
    for i in arr:
        cu_sum+=i
    temp=org_sum-cu_sum
    return temp
print(missingNumber([1,2,4,5],5))