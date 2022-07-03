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

# SET FUNCTION ------------------------------------

# Set funtion to multiply all elements in list together
def prodList(List) :

    # Set product object
    prod = 1
    
    # Multiply elements one at a time
    for i in List:
         prod = prod * i
        
    return prod

# SET PARAMETERS ----------------------------------

# Set max number to loop through, so code is generalisable
maxNum = 20

### CODE ------------------------------------------

# List all possible numbers to check divisibility
allNumbers = list(range(2, maxNum + 1))

### Find prime numbers in allNumbers
# (smallest divisor must be a multiple of the product of all the prime numbers)

# Create empty list to populate
primeNumbers = []

# Loop through allNumbers
for i in allNumbers: 

    # Is the number not divisible by any smaller numbers...
    if not any ( [i % x == 0 for x in range(2, i)] ):
        
        # Then add to list of numbers to use
        primeNumbers = primeNumbers + [i]

### Find smallest divisor

# Set smallest divisor to 0, when this != 0, while loop will stop
minDivisor = 0

# Set first number to check
# (logically smallest divisor must be multiple of prime numbers)
numCheck = prodList(primeNumbers)

# While the smallest divisor has not yet been found...
while minDivisor == 0:
    
    # Divide numCheck by each number and check divisibility
    # i.e. is remainder equal to 0
    isDivisible = [numCheck % x == 0 for x in allNumbers]

    # If numCheck is divisible by every number...
    if all(x == True for x in isDivisible):
        
        # Assign numCheck as the smallest divisor
        minDivisor = numCheck

    # If not found, add prime number product and start loop again
    numCheck = numCheck + prodList(primeNumbers)

# Return solution
print(minDivisor)
