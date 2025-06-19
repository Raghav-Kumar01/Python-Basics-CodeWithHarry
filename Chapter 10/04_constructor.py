class Employ:
    language = "Py" #This is a class attribute
    salary = 1200000

    def __init__(self , name , salary , language): #Dunder method  which is automatically called
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = language    

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employ("Harry" , 1300000 , "Java script")
# harry.name = "Harry"
print(harry.name , harry.language , harry.salary)

# rohan = Employ()

