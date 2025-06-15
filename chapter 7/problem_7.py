'''
for n = 3
  *
 ***
***** 
'''
n = int(input("etner the number:"))

# Ask the user to input the number of rows for the pyramid
n = int(input("Enter the number of rows for the pyramid: "))

# Outer loop runs from 1 to n (inclusive)
for i in range(1, n + 1):

    # Print spaces before the stars to center them
    # For row 1: n-1 spaces, row 2: n-2 spaces, ..., row n: 0 spaces
    print(" " * (n - i), end="")  # end="" means stay on the same line

    # Print stars: number of stars in row i = 2*i - 1 (1, 3, 5, ...)
    print("*" * (2 * i - 1))  # after this, Python moves to the next line by default
