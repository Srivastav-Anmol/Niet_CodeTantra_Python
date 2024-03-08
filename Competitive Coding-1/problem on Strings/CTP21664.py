def isEqualCharacters(s,l):
    i=0
    j=len(s)-1
    while(i<=l):
        if s[i]!=s[j]:
            return False
        elif s[i]==s[j]:
            i+=1
            j-=1
    return True
print("true" if isEqualCharacters(s,l) else "false")