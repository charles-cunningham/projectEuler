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
#

# SET PARAMETERS ----------------------------------

# Starting number must be below which value
maxStart <- 1000000

# FUNCTION ----------------------------------------

# Define function for one chain step of Collatz sequence
collatzFun <- function(value) {
  
  # If input value is even...
  if (value %% 2 == 0) {
    
    # ...divide by 2
    valueOut <- value / 2
    
    # Or else it must be odd, so...
  } else {
    
    # ...multiply by 3 and add 1
    valueOut <- 3 * value + 1
    
  }
  return(valueOut)
}

# SOLUTION ---------------------------------------------    
    
# Create longest sequence objects
longestSeq <- 0 # Sequence length
longestStart <- 0 # Starting number

# Loop through from maxStart/2 to maxStart
# N.B. Longest start must be in this range as numbers < maxStart/2
# can all be obtained by dividing numbers > maxStart /2 by two which
# is a Collatz step [hence Collatz(2n) > Collatz(n)]
for (i in (maxStart/2 + 1): maxStart) {
  
  # Set number to be i, and sequence length to 1
  number <- i
  seqLength <- 1
  
  # While loop to progress through Collatz sequence for i
  while (number > 1) { 
    
    # Move along a stage in Collatz sequence
    number <- collatzFun(number)
    
    # Add one to sequence length
    seqLength <- seqLength + 1
  }
  
  # If sequence length is greater than existing longest length...
  if (seqLength > longestSeq) {
    
    # Update longest length and start number
    longestSeq <- seqLength
    longestStart <- i
  }
}

# Return solution
print(longestStart)

