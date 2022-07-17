# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 3 solution
#
# Script Description: Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# SET PARAMETERS ------------------------------------

# Set number to check prime factors
num = 600851475143

### CODE ------------------------------------------

# Create empty list to add all factors, and seperate list for prime factors
fact = []; pFact = []

# Find square root 
numSqrt = round (num ** (1/2))

# Create list to iterate through to find factors
# (either prime factor or a multiple of prime factor must be in this range)
pFactPoss = list(range(2, numSqrt))

### FIND FACTORS

# Loop through range
for i in pFactPoss: 
    
    # Is num divisible by i?
    if num % i == 0:
        
        # If so, add i and num / i ( also a factor) to list of factors
        fact = fact + [i] + [num / i]

### FIND PRIME FACTORS

# Loop through factors
for i in fact:
    
    # Is the factor only divisible by itself, and no any other factors in list?
    if sum ( [i % x == 0 for x in fact] ) == 1:
        
        # Then add to list of prime factors
        pFact = pFact + [i]
    
# Output solution (largest prime factor)
print(max(pFact))