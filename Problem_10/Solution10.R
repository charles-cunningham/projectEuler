# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 10 solution
#
# Script Description: Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# SET PARAMETERS ----------------------------------

# Set the maximum number
maxN <- 2000000

### CODE ------------------------------------------

# Concept is to loop through all possible numbers -
# removing any larger numbers that are divisible -
# and numbers that are left will be primes

# Set all possible numbers to filter
# (start at 2, first prime number)
primeLs <- c(2: (maxN - 1) )

# Loop through all values up to square root of maxN
# (any number that is NOT prime in primeLs will be divisible by at least one i)
for ( i in 2: floor(sqrt(maxN))) {

  # Subset primeLs to numbers that are either:
  # (a) equal to i, or (b) not divisible by i
  primeLs <- primeLs[ primeLs == i |
                        primeLs %% i != 0 ]
  }

# Sum primes
sumPrimes <- sum(primeLs)

# Return solution
print(sumPrimes)
