"""
CMPS 6100  Lab 1
Author: 
"""

### the only imports needed are here
import math
import time
###

def is_divisible_by(num, i):
    print("num: {} i: {}".format(num,i))
    if((num % i) == 0):
        return True
    else:
        return False
    #pass # remove this line

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(upper_bound):
    if upper_bound < 2:
        return []  # No primes less than 2

    # Initialize a boolean array to keep track of prime status of numbers
    is_prime = [True] * (upper_bound + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    p = 2
    while p * p <= upper_bound:
        if is_prime[p]:
            # Mark all multiples of p as non-prime
            for multiple in range(p * p, upper_bound + 1, p):
                is_prime[multiple] = False
        p += 1

    # Collect all prime numbers
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes


def count_primes(upper_bound):
    count = 0
    for num in range(2, upper_bound + 1):
        if is_prime(num):
            count += 1
    return count


def generate_twin_primes(upper_bound):
    #all prime numbers up to the limit
    primes = generate_primes(upper_bound)
    
    # Find and return twin prime pairs
    twin_primes = [(primes[i], primes[i + 1]) for i in range(len(primes) - 1) if primes[i + 1] - primes[i] == 2]
    
    return twin_primes

def count_twin_primes(upper_bound):
    # Get all prime numbers up to the upper_bound
    primes = generate_primes(upper_bound)
    
    # Count twin prime pairs
    count = 0
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            count += 1
    
    return count 

def largest_twin_primes(upper_bound):
    # Get all prime numbers up to the limit
    primes = generate_primes(upper_bound)
    
    # Find and return the largest twin prime pair
    largest_twin = None
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            largest_twin = (primes[i], primes[i + 1])
    
    return largest_twin

a = largest_twin_primes(100)
print(a)

import time
    
start = time.time()
largest_twin_primes(10)
end = time.time()

elasped_time_ms = (end - start) * 1000
print("Elapsed Time: {:.2f} milliseconds".format(elasped_time_ms))


#########    #########
### Test Functions ###
#########    #########

# You can run them on the terminal.
# The command:
#
# pytest main.py::test_is_divisible_by
#
# Will run the test_is_divisible_by test function.

def test_is_divisible_by():
    assert is_divisible_by(2, 2) == True
    assert is_divisible_by(3, 2) == False
    assert is_divisible_by(47, 7) == False

def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 241, 461, 701, 881, 883, 997]
    for prime in primes:
        assert is_prime(prime) == True
    composites = [4, 6, 8, 9, 10, 25, 30, 36, 39, 49, 60, 64, 121]
    for composite in composites:
        assert is_prime(composite) == False

def test_count_primes():
    assert count_primes(10) == 4
    assert count_primes(100) == 25
    assert count_primes(1000) == 168
    assert count_primes(10000) == 1229

def test_count_twin_primes():
    assert count_twin_primes(10) == 2
    # The two pairs less than 10 are (3,5) and (5,7)
    assert count_twin_primes(100) == 8
    assert count_twin_primes(1000) == 35
    assert count_twin_primes(10000) == 205

test_is_prime()
test_count_primes()
test_is_divisible_by()
test_count_primes()
