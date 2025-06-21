class Animals:
        pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Bow Bow Bow")

c = Dogs()
c.bark()
