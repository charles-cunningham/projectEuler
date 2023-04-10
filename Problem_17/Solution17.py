# HEADER --------------------------------------------
#
# Author: Charles Cunningham
# Email: charles.cunningham@york.ac.uk
# 
# Script Name: Project Euler problem 17 solution
#
# Script Description: Number letter counts
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) 
# contains 20 letters. The use of "and" when writing out numbers is in 
# compliance with British usage.
#

# SET PARAMETERS ----------------------------------

# Set start and stop numbers (only works up to 1000)
startN = 1
stopN = 1000

# SOLUTION ---------------------------------------

# Set lists of numbers (0-9, 10-19, and multiples of 10)
numbers0_9 = ["", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]
numbers10_19 = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numbers10s = ["", "ten", "twenty", "thirty", "forty",
              "fifty", "sixty", "seventy", "eighty", "ninety"]

# Create letter counter
letterCount = 0

# Create digits counter for 1s, 10s, and 100s
count1s = 1
count10s = 0
count100s = 0

# Loop through from startN to stopN inclusive...
for i in range( startN, stopN + 1 ):
    
    ### Create word for number i
    
    # If 1-9...
    if count10s == 0 and count100s == 0: 
        iWord = numbers0_9[count1s]
    
    # If 10-19...
    if count10s == 1 and count100s == 0:
        iWord = numbers10_19[count1s]
    
    # If 20-99
    if count10s > 1 and count100s == 0:
        iWord = numbers10s[count10s] + numbers0_9[count1s]
    
    # If multiple of 100
    if count1s == 0 and count10s == 0 and count100s in range(1, 10): 
        iWord = numbers0_9[count100s] + "hundred" 
    
    # If 101-109, 201-209 etc
    if count1s > 0 and count10s == 0 and count100s in range(1, 10):
        iWord = numbers0_9[count100s] + "hundredand" + numbers0_9[count1s]
    
    # If 110-119, 210-219 etc
    if count10s == 1 and count100s in range(1, 10):
        iWord = numbers0_9[count100s] + "hundredand" + numbers10_19[count1s]
     
    # If 120-199, 220-299 etc
    if count10s > 1 and count100s in range(1, 10):
        iWord = numbers0_9[count100s] + "hundredand" + numbers10s[count10s] + numbers0_9[count1s]

    # Finally, if 1000!
    if count100s == 10:
        iWord = "onethousand"

    # Print current word
    print(iWord)
    
    ### Update counters
    
    # Add letters to letter count
    letterCount = letterCount + len(iWord)
    
    # Update digit counters        
    if count1s < 9: # If 1s are under 9...
        count1s = count1s + 1 # ... add 1 to count1s
    elif count10s < 9:# Otherwise, if 10s are under 9 (i.e. 89 or less) ...
        count1s = 0 # ... reset count1s to 0 ...
        count10s = count10s + 1 # ... and add 1 to count10s
    else: # Otherwise (if 1s and 10s are both 9, i.e. 99) ...
        count1s = 0 # ... reset count1s to 0, ...
        count10s = 0 # ... reset count10s to 0 ...
        count100s = count100s + 1 # ... and add 1 to count100s
               
# Print solution
print(letterCount)
    