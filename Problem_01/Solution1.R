# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 1 solution
#
# Script Description: Multiples of 3 or 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#

# LOAD LIBRARIES -----------------

# LOAD FUNCTIONS ------------------------------------

# SET PARAMETERS ------------------------------------

# Check all numbers less than this value
nMax <- 1000

### CODE ------------------------------------------

# Create object to add to if number is divisible by 3 or 5
iSum <- 0

# Loop through numbers < nMax
for (i in 1:(nMax-1)) {
  
  # If number is exactly divisible by 3 OR 5...
  if (i/3 == round(i/3, digits = 0)|
      i/5 == round(i/5, digits = 0)) {
    
    # ...add i to iSum
    iSum <- iSum + i
    
    }
}

# Solution
iSum