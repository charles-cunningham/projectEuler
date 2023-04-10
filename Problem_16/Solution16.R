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

### LOAD PACKAGES

library(tidyverse)
library(gmp)

# SET PARAMETERS ----------------------------------

# Set base and exponent
base <- 2
exponent <- 1000

# SOLUTION ---------------------------------------

# Find number
# N.B. R cannot deal with extremely large numbers without rounding
# 'gmp' package is needed to deal with these correctly
number <- as.bigz(base) ^ exponent

# Convert number to list of individual digits
digits <- number %>%
  format(., scientific = FALSE) %>%
  as.character %>% # Convert to character string
  strsplit(., "") %>% # Split to digits (outputs list)
  .[[1]] %>% # Convert from list to character vector
  as.integer # Convert to integer vector

# Sum digits
digitSum <- sum(digits)

# Print solution
print(digitSum)
