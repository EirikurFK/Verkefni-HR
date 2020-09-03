# Design an algorithm that generates the first n numbers
# in the following sequence:
# ; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# Store the first 3 numbers of the sequence.
# Add the last 3 numbers together to create a fourth number
# Repeat
# 0,0,0 = 0
# 0,0,1 = 1
# 0,1,1 = 2
# 1,1,1 = 3
# 1,2,3 = 6

n = int(input("Enter the length of the sequence: ")) # Do not change this line

count = 1
while count <= n:
    number1 = 0
    number2 = 0
    number3 = 1
    number4 = number1 + number2 + number3
    print(number4, ", ")
    if number1 = 0 and number4 != 1:
        number1 = 1
    else:
        number1 = number2

    if number2 = 0:
        number2 = 1
    else:
        number2 = number3

    number3 = number4

    count += 1