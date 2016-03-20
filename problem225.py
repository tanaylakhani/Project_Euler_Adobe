# https://en.wikipedia.org/wiki/Trial_division
# https://projecteuler.net/thread=225;post=25698
# Answer: 2009
# Time taken: 0.126959846094

## Approach - Loop from next odd number of 27 through limit count for trial non-divisor
 
import timeit

def check_division(n):
    a = b = c = 1
    num = 0
    while(num <= 3):
        a, b, c = b, c, (a + b + c) % n
        if c == 0:
            return False
        elif c == 1:
            num += 1
        else:
            num = 1
    return True

def problem225(count):
    known_already = [27]
    num = 1
    initial = 27
    while num < count:
        initial += 2
        done = False
        for j in known_already:
            if (initial % j == 0):
                done = True
                break
        if done == True :
            known_already += [initial]
            num += 1
        elif check_division(initial):
            known_already += [initial]
            num += 1      
    print(str(count) + "th non-divisor is: "+format(initial))


if __name__ == '__main__':
    start_time = timeit.default_timer()
    problem225(124)
    elapsed = timeit.default_timer() - start_time
    print("The time taken to execute the code: "+format(elapsed))
    

