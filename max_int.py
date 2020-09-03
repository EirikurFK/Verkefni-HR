# Design an algorithm that finds the maximum positive integer input by a user.
# The user repeatedly inputs numbers until a negative value is entered.

# Initialize a highest number variable
# Compare every input with the highest number variable
# If the current input is higher than the highest number, it becomes
# the highest number.
# If the input is a negative number (< 0), the program prints out the highest
# number and stops.

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0

while num_int > 0:
    if num_int > max_int:
         max_int = num_int
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)    # Do not change this line

#Program complete