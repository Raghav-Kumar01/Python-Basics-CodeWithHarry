class Employ:
    language = "Py" #This is a class attribute
    salary = 1200000

harry = Employ()
harry.name = "Harry" #This is a instance(object) attribute
print(harry.language , harry.salary , harry.name)

rohan = Employ()
rohan.name = "Rohan roro Robinson"
print(rohan.language , rohan.salary , rohan.name)

''' Here name is "instance attribute" and salary and languange is "class attribute" as they
directly belong to the class '''