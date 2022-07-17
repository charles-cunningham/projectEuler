# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 4 solution
#
# Script Description: Largest palindrome product
#
# A palindromic number reads the same both ways. 
#
# The largest palindrome made from the product of two 2-digit 
# numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# SET FUNCTION ------------------------------------

# Create function that outputs TRUE if number if a palindrome, FALSE otherwise
def palindromeCheck(x):
    xRev = int(str(x)[::-1]) # Reverse (x -> character -> reverse -> numeric)
    if (x == xRev): # Check if palindrome
        return True
    if (x != xRev):
        return False
  
# N.B. First line of function uses slice notation on the string - in format
# [start:stop:step]. i.e. [::-1] steps backwards one value at a time,
# and leaving first two parameters blank means step through every value

# SET PARAMETERS ----------------------------------

# Set number of digits to check
digits = 3

### CODE ------------------------------------------

# Create max and min values using number of digits 
maxVal = pow(10,(digits)) - 1
minVal = pow(10,(digits - 1))

# Create object for largest palindrome
palMax = 0

# Loop through the first number between max and min values
for n1 in range(maxVal, minVal - 1, -1):
    
    # Set second number to maxVal
    n2 = maxVal
    
    # While product of both numbers is higher than existing palindrome, continue
    while (n1 * n2 > palMax):
        
        # Check if number is a palindrome, if so...
        if palindromeCheck(n1 * n2) == True:
            
            # Overwrite palMax with product
            palMax = n1 * n2
        
        # Subtract 1 from n2 and begin while loop again   
        n2 = n2 - 1

# Return solution
print(palMax)
