# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 9 solution
#
# Script Description: Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, 
# for which,
#
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# SET PARAMETERS ----------------------------------

# Set the sum of the Pythagorean triplet
abcSum <- 1000

### CODE ------------------------------------------

# Can make some simple logical restrictions on the values a and b can be...
# a: if a + b + c = abcSum, and a < b < c, then a <= (abcSum/3 - 1)
# b: if b + c = abcSum, and b < c, then b <= (abcSum/2 - 1)

# Loop a through 1 to (abcSum/3 - 1)
for ( a in 1 : ( floor(abcSum/3) - 1 )) {
  
  # Loop b through (a + 1) to (abcSum/2 - 1)
  for ( b in (a + 1) : (floor(abcSum/2) - 1 )) {
  
  # Calculate c from a and b
  c <- abcSum - a - b
  
  # If a^2 + b^2 = c^2...
  if ( ( a^2 + b^2 ) == c^2 ) {
    
    # Save the product of a, b, c (and a, b, c themselves)
    abcProd <- a * b * c
    aTriplet <- a; bTriplet <- b; cTriplet <- c
    
    # Output solution
    print(abcProd); print( c(aTriplet, bTriplet, cTriplet ))
    
    }
  }
}
  