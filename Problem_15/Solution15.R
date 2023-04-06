# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 15 solution
#
# Script Description: Lattice paths
#
# Starting in the top left corner of a 2×2 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the 
# bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#

# SET PARAMETERS ----------------------------------

# Grid size (i.e. length of one side of *square* grid)
gridLength <- 20

# SOLUTION ---------------------------------------

# Initially tried manually creating combinations of "right" and "down", 
# but too many to solve by this method. 
# Instead, idea is to use combination logic to solve. We want to pick an equal 
# number of "down" and "right" from route length to end up at bottom right. 
# Hence can reformulate 'n choose r' equation, i.e. n! / (n - r)! * r! into:
# N.B. grid is square so route length is gridLength x 2 and n-r == r
nRoutes <- factorial(gridLength * 2) / (factorial(gridLength) ^ 2 )

# Print solution
print(nRoutes)
