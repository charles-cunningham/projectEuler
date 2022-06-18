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
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# SET FUNCTION ------------------------------------

# Create function that outputs TRUE if number if a palindrome, FALSE otherwise
palindromeCheck <- function(x) {
  
  # Reverse numbers (x -> character -> split -> reverse -> merge -> numeric)
  xRev <- format(x, scientific = FALSE)
  xRev <- as.character(xRev)
  xRev <- strsplit(xRev, "")[[1]]
  xRev <- rev(xRev)
  xRev <- paste0(xRev, collapse = "")
  xRev <- as.numeric(xRev)

  # Check if palindrome
if (x == xRev) { return(TRUE) } 
if (x != xRev) { return(FALSE) }
  
}

# SET PARAMETERS ----------------------------------

# Set number of digits to check
digits <- 3

### CODE ------------------------------------------

# Create max and min values using number of digits 
maxVal <- 10^(digits) - 1
minVal <- 10^(digits - 1)

# Create object for largest palindrome
palMax <- 0

# Loop through the first number between max and min values
for (n1 in maxVal:minVal) {
  
  # Set second number to maxVal
  n2 <- maxVal
  
  # While product of both numbers is higher than existing palindrome, continue
  while (n1 * n2 > palMax) {

    # Check if number is a palindrome, if so
    if(palindromeCheck(n1 * n2) == TRUE) {
      
      # Overwrite palMax with product
      palMax <- n1 * n2 }
    
    # Subtract 1 from n2 and begin while loop again   
    n2 <- n2 - 1
    
  }}

# Return solution
print(palMax)
