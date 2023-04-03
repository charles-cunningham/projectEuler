# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 14 solution
#
# Script Description: Longest Collatz sequence
#
# The following iterative sequence is defined for 
# the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

# FUNCTION ----------------------------------------

# Define function for one chain step of Collatz sequence
def collatzFun(value) :
    
    # If input value is even...
    if (value % 2 == 0):
        
        # ...divide by 2
        valueOut = value / 2
    
    # Or else it must be odd, so...
    else: 
        
        # ...multiply by 3 and add 1
        valueOut = 3 * value + 1
    
    return valueOut

# SET PARAMETERS ----------------------------------

# Starting number below which value
maxStart = 1000000

### CODE ------------------------------------------

# Create longest sequence object
longestSeq = 0
longestStart = 0

#
for i in range( int(maxStart/2), maxStart ):

    #
    number = i
    seqLength = 1

    #
    while (number > 1):
        
        #
        number = collatzFun(number)
        
        #
        seqLength = seqLength + 1

    #
    if (seqLength > longestSeq):
        
        #
        longestSeq = seqLength
        longestStart = i

# Return solution
print(longestStart)
