a = int(input("Enter no. 1:"))
b = int(input("Enter no. 2:"))
if b==0 :
    raise ZeroDivisionError("hey you cannot put 0 in b")
else:
    print(f"The division of a/b is:{a/b}")