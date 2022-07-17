# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 3 solution
#
# Script Description: Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# SET PARAMETERS ------------------------------------

# Set number to check prime factors
num <- 600851475143

### CODE ------------------------------------------

# Create empty list to add all factors, and seperate list for prime factors
fact <- c(); pFact <- c()

# Find square root of 'num' (round down)
numSqrt <- floor(sqrt(num))

### FIND FACTORS

# Loop through range to find factors
# (either prime factor or a multiple of prime factor must be in this range)
for (i in 2:numSqrt) { 
  
  # Is num divisible by i?
  if ( num/i == round( num/i, digits = 0)) {
  
  # If so, add i and num / i ( also a factor) to list of factors
  fact <- c( fact, i, num/i)
  
  }
}
  
### FIND PRIME FACTORS

# Loop through factors
for (i in 1:length(fact)) {
  
  # Divide i by all other factors
  factCheck <- fact[i] / fact[-i]
  
  # Check if i is not divisible by any other factor in list
  if ( !any(factCheck == round( factCheck, digits = 0 ))) {
  
  # If so, add to list of prime factors
  pFact <- c(pFact, fact[i])
  
  }
}

# Output solution (largest prime factor)
print(max(pFact))