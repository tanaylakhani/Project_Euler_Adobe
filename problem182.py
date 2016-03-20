#https://books.google.com/books?id=8eLiBwAAQBAJ&lpg=PA69&ots=PQJN3aBz_U&dq=The%20number%20of%20unconcealed%20messages%20is%20given%20by&pg=PA69#v=onepage&q=The%20number%20of%20unconcealed%20messages%20is%20given%20by&f=false

# https://vilhena.wordpress.com/2010/05/31/problem-182/ -- suggests better approach for performance but needs more reading into cryptography
# from gmpy2 import gcd - gives better performance but its an external library

# Answer: 399788195976
# Time taken: 4.28784930318

## Approach - The number of unconcealed messages is given by (1 + GCD(e-1, p-1))*(1 + GCD(e-1,q-1)). (from the above google book result)

from fractions import gcd
import timeit

def problem182():
    p,q = 1009,3643
    n = p * q
    phi = (p-1)*(q-1)
    res = 0
    min_res = p*q+1;
    for e in range(1, phi):
        if(gcd(e,phi)!=1): continue;
        no_unconcealed_messages = (1 + gcd(e-1, p-1)) * (1 + gcd(e-1, q-1))
        if no_unconcealed_messages == min_res:
            res += e
        elif no_unconcealed_messages < min_res:
            min_res = no_unconcealed_messages
            res = e
    print("The sum is: "+format(res))

if __name__ == '__main__':
    start_time = timeit.default_timer()
    problem182()
    elapsed = timeit.default_timer() - start_time
    print("The time taken to execute the code: "+format(elapsed))
