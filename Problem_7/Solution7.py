# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 7 solution
#
# Script Description: 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# SET PARAMETERS ----------------------------------

# Set max number 
maxN = 10001

### CODE ------------------------------------------

# Create list of prime numbers and populate with first prime number - 2
primes = [2]

# Start prime number search with the first odd number after two - 3
n = 3

# While the prime number list length is less than the length we want...
while len(primes) < maxN:

    # Subset primes to those less than the square root of n to speed up
    # ( n must be prime if it is not divisible by any of these )
    sqrtPrimes = [x for x in primes if x <= pow(n, 1/2)]

    # If n is not divisible by any numbers in sqrtPrimes
    if not any( n % x == 0 for x in sqrtPrimes ):
        
        # Add n to the list of primes
        primes = primes + [n]

    # Add 2 to n (keep it odd) and restart loop
    n = n + 2

# Return solution (last number in primes)
print(primes[-1])
