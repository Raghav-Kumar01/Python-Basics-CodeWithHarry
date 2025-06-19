from random import randint
class Train:
    def __init__(self , trainNo):
        self.trainNo = trainNo

    def book(self ,  fro , to):
        print(f"Ticket is booked in TrainNo.{self.trainNo} FROM {fro} To {to}")

    def getstatus(self ,):
        print(f"TrainNo.{self.trainNo} is running on time")

    def getFare(self ,  fro , to):
        print(f"Ticket is booked in train number:{self.trainNo} form {fro} to {to} fare is {randint(1 , 5555)}")
t = Train(2323)
t.book("Rampur", "Delhi")
t.getstatus()
t.getFare("Rampur", "Delhi")
