class Employ:
    language = "Py" #This is a class attribute
    salary = 1200000

harry = Employ()
harry.language = "Java" #This is a instance(object) attribute
print(harry.language , harry.salary )
