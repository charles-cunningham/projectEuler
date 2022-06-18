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
nMax = 1000

### CODE ------------------------------------------

# Add sum of numbers divisible by 3 or 5 to this object
iSum = 0

# Loop numbers less than nMax
for i in range(1,nMax):
    
    # If i/3 and i/5 have no remainder (divisible) then...
    if i/3 % 1 == 0 or i/5 % 1 == 0:
        
        # ...add i to iSum
        iSum = iSum + i

# Output solution
print(iSum)