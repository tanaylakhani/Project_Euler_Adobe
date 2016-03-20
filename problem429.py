# http://mathworld.wolfram.com/UnitaryDivisorFunction.html
# referenced - https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p429.py
# using better sieve implementation to generate prime can speed up execution
# Answer: 98792821
# Time taken: 31.9265199866

## Approach - Find all the primes up to 10^8 (with a sieve). Factorize using http://www.cut-the-knot.org/blue/LegendresTheorem.shtml and then use the Unitary Divisor Function

import math
import timeit

MOD = 1000000009

## Generate Primes
def pfast(N):
    siz = N // 2
    isprim = [True] * (siz)
    plst = [2]
    for i in range(1, int(math.sqrt(N)) // 2 + 2):
        if isprim[i]:
            p = i + i + 1
            j = i + p
            while j < siz:
                isprim[j] = False
                j += p
    p = 3
    for i in range(1, siz):
        if isprim[i]:
            plst.append(p)
        p += 2    
    return plst

## Generate primes using sieve - saves 9 seconds from earlier implementation
def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def check_factorial(n, p):
    count = []
    for x in xrange(1, int  (math.log(n, p)) + 1):
        count.append(n / (p ** x))
    return sum(count)

def problem429(N):
    # primes = pfast(N)
    primes = rwh_primes(N)
    seq = []
    for p in primes:
        seq.append(1 + pow(p, 2 * check_factorial(N, p), MOD))
    ans = reduce(lambda k, m: (k * m) % MOD, seq)
    print 'The result is: '+format(ans) 

if __name__ == '__main__':
    start_time = timeit.default_timer()
    problem429(10**8)
    elapsed = timeit.default_timer() - start_time
    print("The time taken to execute the code: "+format(elapsed))