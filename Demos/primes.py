import os
os.system("")
import math as m
import time
print("\n")
def get_primes(a,b):
    res = []
    for x in range(max(a,2),b+1):
        fact = False
        for p in range(2,int(m.sqrt(x)) + 1):
            if x % p ==0:
                fact = True
                break
        if not fact:
            res.append(x)
    return res
def primeratio(a,b):
    primes = get_primes(a,b)
    return len(primes)/len(range(a,b+1))
def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

rang = 10**(3*4)
ran = 10**(3*3)
#start = time.time()
primes1000 = get_primes(0,ran)
#end = time.time()
print("GetPrimes",len(primes1000))
start = time.time()
primest = primes2(ran)
end = time.time()
print("primes2",end-start)

