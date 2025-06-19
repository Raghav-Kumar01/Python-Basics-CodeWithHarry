class Demo:
    a = 4
o = Demo()
print(o.a)#Prints class attribute because instance attrubute is not present
o.a = 0   #Instance attribute is set
print(o.a)#Prints Instance attribute because instance attrubute is present
print(Demo.a)#Prints the class attribute
