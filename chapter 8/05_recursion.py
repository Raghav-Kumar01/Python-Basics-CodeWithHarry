'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n x (n-1) x ..................

factorial(n) = n * factorial(n-1)
'''
def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factorial(n-1)

n = int(input("enter a number here:"))
print(f"the factorial of this number is:{factorial(n)}")