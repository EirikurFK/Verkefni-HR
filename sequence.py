# Store the first 3 numbers of the sequence.
# Add the last 3 numbers together to create a fourth number
# Repeat
# 1: 0,0,1 = 1
# 2: 0,1,1 = 2
# 3: 0,1,2 = 3
# 4: 1,2,3 = 6
# 5: 2,3,6 = 11
# 6: 3,6,11 = 20
# 7: 6,11,20 = 37
n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1 = 0
n2 = 1
n3 = 0
count = 0

while count < n:
    nt = n1 + n2 + n3
    print(nt)
    n1 = n2
    n2 = n3
    n3 = nt
    

    count += 1