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

### IMPORT LIBRARIES

# Import NumPy
import itertools

# SET PARAMETERS ----------------------------------

# Grid size (stay below 5 for testing)
gridLength = 5

# SOLUTION ---------------------------------------

# Specify movement options
movement = ['Right', 'Down']

# Route length
# (how many moves to get from top left to bottom right)
routeLength = gridLength * 2

# Calculate all possible movement permutations
allPerms = list( itertools.product(movement,
                                   repeat = routeLength) )

# Remove 'impossible' movements,
# i.e. ones which go off the edge of the grid
possiblePerms = [i for i in allPerms if 
                 i. count("Right") == gridLength and 
                 i. count("Down") == gridLength ]

# Return solution
print(len(possiblePerms))
