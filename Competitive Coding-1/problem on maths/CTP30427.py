def isDivisibleBy41(d1,d2,c,L):
    digits=[d1,d2]+[0]*(L-2)
    for i in range(2,L):
        digits[i]=(digits[i-1]*c+digits[i-2])%10
    num=0
    for i in range(L):
        num+=digits[i]*10**(L-i-1)
    return num%41==0
print("true" if isDivisibleBy41(d1,d2,c,L) else "false")