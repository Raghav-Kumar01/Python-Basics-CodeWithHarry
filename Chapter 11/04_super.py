class Employ:
    def __init__(self):
        print("Constructor of Employ")
    a= 1
class programer(Employ):
    def __init__(self):
        print("Constructor of programer")
    b = 2
class manager(programer):
     def __init__(self):
        super().__init__()
        print("Constructor of manager")
     c = 3

# o = Employ()
# print(o.a)#prints the a attribute

# o = programer()
# print(o.a , o.b)

o = manager()
print(o.a , o.b , o.c)
