maths = int(input("enter your maths marks here:"))
physics = int(input("enter your maths marks here:"))
chemistry = int(input("enter your maths marks here:"))
total = (maths+physics+chemistry)
print("total marks are:", total)

if(maths>=33 and physics>=33 and chemistry>=33 and total>=120 ):
    print("passed")
else:
    print("failed")