# Design an algorithm that generates the first n numbers
# in the following sequence:
# ; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# Store the first 3 numbers of the sequence.
# Add the last 3 numbers together to create a fourth number
# Repeat

n = int(input("Enter the length of the sequence: ")) # Do not change this line

number_1 = 1
number_2 = 1
number_3 = 1

print number