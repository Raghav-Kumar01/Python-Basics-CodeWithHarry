try:
    a = int(input("Enter a Number:"))
except ValueError as v:
    print(v)
    print("heyyy")
except Exception as e:
    print(e)
print("Thankyou")