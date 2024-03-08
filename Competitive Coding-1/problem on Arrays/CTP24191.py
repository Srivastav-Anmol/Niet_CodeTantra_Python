def lengthIndexMatch(arr):
    n=len(arr)
    ans=""
    for i in range(n):
        if len(arr[i])==i:
            ans+=str(arr[i])
    if len(ans)!=0:
        return ans
    else:
        return "no match found"
    
print(lengthIndexMatch(arr))