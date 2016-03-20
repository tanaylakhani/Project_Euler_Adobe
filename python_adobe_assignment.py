import problem225
import problem429
import problem182
import timeit

if __name__ == "__main__":
    print("Project Euler #182:")
    start_time = timeit.default_timer()
    problem182.problem182()
    elapsed = timeit.default_timer() - start_time
    print("The time taken to execute #182: "+format(elapsed))
    print("Project Euler #225:")
    start_time = timeit.default_timer()
    problem225.problem225(124)
    elapsed = timeit.default_timer() - start_time
    print("The time taken to execute the #225: "+format(elapsed))
    print("Project Euler #429:")
    start_time = timeit.default_timer()
    problem429.problem429(10**8)
    elapsed = timeit.default_timer() - start_time
    print("The time taken to execute the #429: "+format(elapsed))
    