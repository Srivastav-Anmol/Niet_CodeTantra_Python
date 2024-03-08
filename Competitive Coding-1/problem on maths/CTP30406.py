def getProductSign(a,b):
    sign="Positive"
    pro=1

    if a>b:
        a,b=b,a
    if a==0 or b==0:
        return "zero"
    if a>0 and b>0:
        return "positive"
    if (a>0 and b<0) or (a<0 and b>0):
        return "zero"
    elif ((a-b)+1)%2==0:
        return "positive"
    elif ((a-b)+1)%2!=0:
        return "negative"
    
print(getProductSign(a,b))