class Employ:
    comapny = "ITC"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

# class Programer:
#     company = "ITC infosis"
#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")
    
#     def language(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
class Programer(Employ):
     company = "ITC infosis"
     def language(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employ()
b = Programer()

print(a.comapny , b.company)