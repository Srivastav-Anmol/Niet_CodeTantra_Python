def getFirstSubString(s,l):
    ans=""
    for i in range(0,len(s),2):
        ans+=s[i]
        if len(ans)>=l:
            return ans
    return "NotFound"
print(getFirstSubString(s,l))