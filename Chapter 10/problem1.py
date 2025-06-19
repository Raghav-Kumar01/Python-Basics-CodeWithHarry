class Programing:
    company = "Microsoft"
    def __init__(self , name , salary , age):
        self.name = name
        self.salary = salary
        self.age = age
        

p = Programing("Harry" , 1233343 , 18)
print(p.name , p.company , p.age)