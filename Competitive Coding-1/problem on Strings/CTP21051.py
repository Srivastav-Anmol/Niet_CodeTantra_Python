def isPrimeLenghtPalindrome(s):
    temp=""
    n=len(s)
    flag=0
    if n>1:
        for i in range(2,n):
            if n%i==0:
                flag=1
                break
    if flag==1:
        return False
    else:
        for i in s:
            temp=i+temp
        if temp==s and flag==0:
            return True
        else:
            return False
        
print("true" if isPrimeLenghtPalindrome else "false")