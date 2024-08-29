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

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
num = 8
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

def is_prime(num):
    # Handle edge cases
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check for factors from 5 to sqrt(n)
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
is_prime(3)

def generate_primes(upper_bound):
    # TO-DO
    # Implement this function
    pass # remove this line

def count_primes(upper_bound):
    count = 0
    for num in range(2, upper_bound + 1):
        if is_prime(num):
            count += 1
    return count

def generate_twin_primes(upper_bound):
    # TO-DO
    # Implement this function
    pass # remove this line

def count_twin_primes(upper_bound):
    # TO-DO
    # Implement this function
    pass # remove this line

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