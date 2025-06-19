class Employ:
    a= 1
class programer(Employ):
    b = 2
class manager(programer):
    c =  3

o = Employ()
print(o.a)#prints the a attribute
# print(o.b)# shows an error as there is no b attribute employ class

o = programer()
print(o.a , o.b)

o = manager()
print(o.a , o.b , o.c)
