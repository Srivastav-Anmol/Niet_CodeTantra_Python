def reverseAlphas(S):
    l=list(S)
    i=0
    j=len(S)-1
    while i<j:
        if not l[i].isalpha():
            i+=1
        elif not l[j].isalpha():
            j-=1
        else:
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
    out=''.join(l)
    return out
print(reverseAlphas(S))