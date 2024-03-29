# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 16 solution
#
# Script Description: Power digit sum
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#

### IMPORT LIBRARIES

# SET PARAMETERS ----------------------------------

# Set base and exponent
base = 2
exponent = 1000

# SOLUTION ---------------------------------------

# Find number
number = base ** exponent

# Convert number to list of individual digits
digits = [int(x) for x in str(number)]

# Sum digits
digitSum = sum(digits)

# Print solution
print(digitSum)
