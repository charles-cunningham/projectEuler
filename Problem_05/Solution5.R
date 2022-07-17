# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 5 solution
#
# Script Description: Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

# SET PARAMETERS ----------------------------------

# Set max number to loop through, so code is generalisable
maxNum <- 20

### CODE ------------------------------------------

# List all possible numbers to check divisibility
allNumbers <- c(2:maxNum)

### Find prime numbers in allNumbers
# (smallest divisor must be a multiple of the product of all the prime numbers)

# Create empty list to populate
primeNumbers <- c()

# Loop through allNumbers
for (i in allNumbers) {
  
  # Loop through numbers from 2 up to (but not including) i...
  isDivisible <- sapply( c(2:(i-1)) ,
                         
                         # Check divisibility of i by each number
                         function (x) { i %% x == 0 })
   
   # If not divisible by any smaller numbers...
   if (!any(isDivisible)) {
     
     # ...add to list of numbers to use
     primeNumbers <-  c(primeNumbers, i)
     
     }}

### Find smallest divisor

# Set smallest divisor to 0, when this != 0, while loop will stop
minDivisor <- 0

# Set first number to check
# (logically smallest divisor must be multiple of prime numbers)
numCheck <- prod(primeNumbers)

# While the smallest divisor has not yet been found...
while (minDivisor == 0) {
  
  # Loop through allNumbers...
  isDivisible <-  sapply(allNumbers,
                         # Check divisibility of numCheck by each number
         function (x) { numCheck %% x == 0 })
  
  # If numCheck is divisible by every number...
  if (all(isDivisible)) {

    # Assign numCheck as the smallest divisor
    minDivisor = numCheck
    
    }
  
  # If not found, add prime number product and start loop again
  numCheck <- numCheck + prod(primeNumbers)

}

# Return solution
print(minDivisor)
