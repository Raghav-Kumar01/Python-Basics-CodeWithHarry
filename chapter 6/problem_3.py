p1 = "make a lot of money" 
p2 = "buy now"
p3 = "click this" 
comment = input("enter the statement:")

if ( p1 in comment or p2 in comment or p3 in comment):
    print("this is spammer")
else:
    print("this is not spammer")
