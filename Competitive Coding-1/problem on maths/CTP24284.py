def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def primeSum(n):
    primes=[]
    for i in range(2,n+1):
        if isprime(i):
            primes.append(i)
    sum=primes[0]
    counter=0
    for i in range(1,len(primes)):
        sum+=primes[i]
        if sum<=n and isprime(sum):
            counter+=1
        if sum>n:
            break
    return counter
print(primeSum(n))