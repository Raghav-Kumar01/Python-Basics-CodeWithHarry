a1 = int(input("enter no. 1 :"))
a2 = int(input("enter no. 2 :"))
a3 = int(input("enter no. 3 :"))
a4 = int(input("enter no. 4 :"))

if(a1>a2 and a1>a3 and a1>a4):
    print("the greatest number is a1",a1)
if(a2>a1 and a2>a3 and a2>a4):
    print("the greatest number is a2",a2)
if(a3>a2 and a3>a1 and a3>a4):
    print("the greatest number is a3",a3)
if(a4>a2 and a4>a3 and a4>a1):
    print("the greatest number is a4",a4)

    #WE NOT USE OR HERE BECAUSE IF ONE CONDITION CAME TRUE 
    # IT RUN IF FUNCTION BUT AND WHEN ALL CONDITION CAME TRUE THEN RUN IF FUNCTION
# if(a1>a2 or a1>a3 or a1>a4):
#     print("the greatest number is a1",a1)
# if(a2>a1 or a2>a3 or a2>a4):
#     print("the greatest number is a2",a2)
# if(a3>a2 or a3>a1 or a3>a4):
#     print("the greatest number is a3",a3)
# if(a4>a2 or a4>a3 or a4>a1):
#     print("the greatest number is a4",a4)