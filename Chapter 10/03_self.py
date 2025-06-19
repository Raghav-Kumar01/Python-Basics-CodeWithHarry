class Employ:
    language = "Py" #This is a class attribute
    salary = 1200000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employ()
harry.language = "Java" #This is a instance(object) attribute
print(harry.language , harry.salary )
harry.getinfo() # is same as ,Employ.getinfo(harry)
harry.greet()

