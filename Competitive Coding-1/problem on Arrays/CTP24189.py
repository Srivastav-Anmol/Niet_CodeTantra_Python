def maxSumContiguousSubArray(arr):
    sum=0
    maxi=arr[0]
    n=len(arr)
    for i in range(n):
        sum+=arr[i]
        maxi=max(sum,maxi)
        if sum<0:
            sum=0
    return maxi
print(maxSumContiguousSubArray(arr))