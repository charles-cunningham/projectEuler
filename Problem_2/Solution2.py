# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 2 solution
#
# Script Description: Even Fibonacci numbers
#
# Each new term in the Fibonacci sequence is generated by adding the 
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.
#

# SET PARAMETERS ------------------------------------

# Fibonacci numbers cannot exceed this value
maxN = 4000000

### CODE ------------------------------------------

# Set initial Fibonacci numbers to start
fibList = [1,2]

# While the last Fibonacci value is below maxN...
while fibList[len(fibList) - 1] < maxN:
    
    # Create a new Fibonacci number (sum of previous two Fibonacci numbers)...
    fibN = fibList[len(fibList) - 1] + fibList[len(fibList) - 2]
    
    # ...and add to list
    fibList = fibList + [fibN]

# Remove last value as the while loop overshoots by 1
fibList = fibList[0: len(fibList) - 1]

#  Subset to even numbers
fibListEven = [x for x in fibList if x/2 % 1 == 0]

# Sum and print solution
print( sum( fibListEven ))