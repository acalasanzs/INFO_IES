import math
import itertools
import time
def factors(num):
    factors = []
    num = 30
    for x in range(1,num+1):
        if num % x == 0:
            factors.append(x)
    return factors
  
# A function to print all prime factors of 
# a given number n
def primeFactors(n):
    f = []
    while n % 2 == 0:
        f.append(2),
        n = n / 2
          
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
          
        # while i divides n , print i ad divide n
        while n % i== 0:
            f.append(i),
            n = n / i
              
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        f.append(int(n))
    return f
def M(p,q,lim):
    i = lim
    while True:
        prime = primeFactors(i)
        #if all(x in prime for x in [p, q]):
        if all(x in (p, q) for x in prime) and p in prime and q in prime:
            return i
        else:
            i -= 1
        if i < 2:
            return 0
#print(M(3,5,100))
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
def S(N):
    primes = primes2(100)
    print("Primes got")
    result = 0
    combinations = []
    for subset in itertools.combinations(primes, 2):
        if not subset[0] == subset[1]:
            combination = f"M({subset[0]},{subset[1]},{N})"
            print(combination)
            combinations.append(combination)
            res = M(subset[0],subset[1],N)
            result += res
            print(res,result)
    """ for i,item in enumerate(primes):
        if len(primes) == i+1:
            break
        print(item,primes[i+1])
        result += M(item,primes[i+1],N) """
    return result
def S0(N):
    # Get all primes below N, divided by 2 bc 2 is the smallest prime
    primes = primes2(int(N/2))

    result = 0
    # For loop of all combinations in tuple length 2 of primes
    for subset in itertools.combinations(primes, 2):
        #Comprovar que no sigui una combinació reptida. E. g.: (3,3) or (5,5)
        if not subset[0] == subset[1]:
            result += M(subset[0],subset[1],N)

    return result
def S3(N):
    # Get all primes below N, divided by 2 bc 2 is the smallest prime
    primes = primes2(int(N/2))
    #print(len(primes)*11.907)
    result = 0
    start = time.time()
    # For loop of all combinations in tuple length 2 of primes
    for subset in itertools.combinations(primes, 2):
        #Comprovar que no sigui una combinació reptida. E. g.: (3,3) or (5,5)
        if not subset[0] == subset[1]:
            result += M(subset[0],subset[1],N)
        if subset[0] > 2:
            end = time.time()
            time2reach = end-start
            print(time2reach)
            print(time2reach*len(primes))
            quit()
    end = time.time()
    print(end-start)
    return result
def S2(N):
    primes = primes2(N)
    f = open("Demos/Calculation of S2.txt","w")
    f.write("S({})\n\n\n".format(N))
    f.close
    result = 0
    for subset in itertools.combinations(primes, 2):
        f = open("Demos/Calculation of S2.txt","a")
        if not subset[0] == subset[1]:
            combination = f"M({subset[0]},{subset[1]},{N})\n\n"
            f.write(combination)
            res = M(subset[0],subset[1],N)
            result += res
            f.write("{}     {}\n".format(res,result))
            f.close()
    return result
print(S3(10000000))
# S(100) = 2262
""" stuff = primes2(10)
for subset in itertools.combinations(stuff, 2):
    print(subset) """