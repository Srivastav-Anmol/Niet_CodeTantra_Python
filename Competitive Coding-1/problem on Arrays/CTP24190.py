def pairOfSum(arr,s):
    ans=""
    count=0
    for i in range(len(arr)):
        temp=arr[i]
        for j in range(i+1,len(arr)):
            if temp+arr[j]==s:
                count+=1
                ans+="<"+str(i)+","+str(j)+">"+","
        if count>0:
            return ans[0:len(ans)-1]
        else:
            return "no such pairs"
        
print(pairOfSum(arr))