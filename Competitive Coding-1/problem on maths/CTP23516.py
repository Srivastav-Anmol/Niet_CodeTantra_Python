def sumOfPairs(n1,n2):
    su=0
    n1,n2=sorted([n1,n2])
    for i in range(n1,n2+1):
        count=0
        if i==1:
            continue
        for j in range(2,i):
            if i%j==0:
                count=1
                break
        if count==0:
            su+=i
    return su