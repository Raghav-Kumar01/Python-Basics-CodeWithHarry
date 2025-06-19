class Employ:
    comapny = "ITC"
    name = "default name"
    def show(self):
        print(f"The name is {self.name} and salary is {self.comapny }")

class coder:
    language = "python"
    def printlanguage(self):
        print(f"out of other language here is your language:{self.language}")

# class Programer:
#     company = "ITC infosis"
#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")
    
#     def language(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
class Programer(Employ , coder):
     company = "ITC infosis"
     def showlanguage(self):
        print(f"The name is {self.comapny} and he is good with {self.language} language")

a = Employ()
b = Programer()

b.show()
b.showlanguage()
b.printlanguage()
