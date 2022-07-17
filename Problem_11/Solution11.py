# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 11 solution
#
# Script Description: Largest product in a grid
#
# In the 20×20 grid below, four numbers along a 
# diagonal line have been marked in red.
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# 
# What is the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20×20 grid?

### IMPORT LIBRARIES

# Import NumPy
import numpy as np

# SET PARAMETERS ----------------------------------

# Set the grid (paste between triple quotes)
xyGridRaw = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

# Set number of adjacent numbers to check
numAdj = 4

### CODE ------------------------------------------

### Read in grid

# Count number of rows using line breaks
nRow = xyGridRaw.count('\n') - 1

# Read as NumPy array
# (convert to single array using spaces, then reshape to 2D array)
xyGrid = np.fromstring(xyGridRaw, sep=' ').reshape(nRow, -1)

# Find number of columns
nCol = len(xyGrid[0])

### Create solution objects to populate

# Set greatest product to 0, this will be overwritten
maxProd = 0

# Set empty vector to fill with [i,j] of max value
maxCoord = []

# Set empty vector to fill with associated adjacent numbers
maxAdj = []

### Loop through every value in array to greatest product

# Loop through rows...
for i in range(0, nRow):
    # Loop through columns...
    for j in range(0, nCol):
        
        # Reset empty arrays for the adjacency arrays
        adjN = adjNE = adjE = adjSE = adjS = adjSW = adjW = adjNW = []

        # Starting with North, work clockwise through every possible
        # combination of adjacent numbers. IF statements needed to prevent
        # including directions that would go 'off the edge'
        
        # NORTH
        
        # Row number must be high enough to populate array fully
        if i > (numAdj - 2):
            # Get values 'above' [i,j]
            adjN = xyGrid[i-(numAdj-1) : i+1, j]
        # Switch order to start from [i,j]
        adjN = adjN[::-1] 
        
        # NORTHEAST
        
        # Row number must be high enough, and column number low enough
        if i > (numAdj - 2) and j < (nCol + 1 - numAdj) :
            # Need to use small loop for diagonals
            for x in range(0, numAdj):
                # Move incrementally 'up' (i-x) and 'right' (j+x)
                adjNE = adjNE + [xyGrid[ i -x , j+x ]] 
            # Convert to array
            adjNE = np.array(adjNE)
            
        # Rest of directions follow same approach, not commented
        
        # EAST
        if j < (nCol + 1 - numAdj):
            adjE = xyGrid[i, j : j+numAdj]
        
        # SOUTHEAST
        if i < (nRow + 1 - numAdj) and j < (nCol + 1 - numAdj) :
            for x in range(0, numAdj):
                adjSE = adjSE + [xyGrid[ i+x , j+x ]]  
            adjSE = np.array(adjSE)  
        
        # SOUTH
        if i < (nRow + 1 - numAdj):
            adjS = xyGrid[i : i+numAdj, j]
        
        # SOUTHWEST
        if i < (nRow + 1 - numAdj) and j > (numAdj - 2):
            for x in range(0, numAdj):
                adjSW = adjSW + [xyGrid[ i+x , j-x ]]  
            adjSW = np.array(adjSW)  
        
        # WEST
        if j > (numAdj - 2):
            adjW = xyGrid[i, j-(numAdj-1) : j+1]
            adjW = adjW[::-1]
        
        # NORTHWEST
        if i > (numAdj - 2) and j > (numAdj - 2):
            for x in range(0, numAdj):
                adjNW = adjNW + [xyGrid[ i-x , j-x ]]  
            adjNW = np.array(adjNW)  
        
        # Combine all adjacent values in every direction into one array 
        adjAll = [[adjN],[adjNE],[adjE],[adjSE],
                  [adjS],[adjSW],[adjW],[adjNW]]
        
        # Find product of adjacent values in every direction
        prodAll = list(map(np.prod, adjAll))
        
        # If product is higher than previous maximum,
        # overwrite all solution objects
        if (max(prodAll) > maxProd):
            
            maxProd = max(prodAll)
            maxCoord = [i,j]
            maxAdj = adjAll[np.argmax(prodAll)]
    
# Return solution
print("The greatest product is", maxProd,
      "starting at row", maxCoord[0],
      "and column", maxCoord[1], 
      "with values", maxAdj)
