from time import time

def time_function(f, i):
    """
    returns the time it takes to run function f with input i
    """
    start = time()
    f(i)
    end = time()
    elapsed = end - start
    print(elapsed, ' seconds have elapsed for ', f, ' with input ', i)
    return elapsed

if __name__ == '__main__':

    from Sieve_of_Eratosthenes import Sieve_of_Eratosthenes
    from Sieve_of_Eratosthenes import fast_Sieve_of_Eratosthenes
    from Sieve_of_Eratosthenes import Sieve_of_Eratosthenes_numpy

    time_function(Sieve_of_Eratosthenes, 1000000)
    time_function(fast_Sieve_of_Eratosthenes, 1000000)
    time_function(Sieve_of_Eratosthenes_numpy, 1000000)

