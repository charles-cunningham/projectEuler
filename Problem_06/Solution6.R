# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 6 solution
#
# Script Description: Sum square difference
#
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

# SET PARAMETERS ----------------------------------

# Set max number to find sum of squares
maxNum <- 100

### CODE ------------------------------------------

# Find sum of squares
sumSq <- sum((1:100)^2)

# Find square of the sum
sqSum <- sum(1:100)^2

# Find difference
diff = sqSum - sumSq

# Return solution
print(diff)
