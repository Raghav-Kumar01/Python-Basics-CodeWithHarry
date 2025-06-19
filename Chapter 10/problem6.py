from random import randint
class Train:
    def __init__(slf , trainNo):
        slf.trainNo = trainNo

    def book(slf ,  fro , to):
        print(f"Ticket is booked in TrainNo.{slf.trainNo} FROM {fro} To {to}")

    def getstatus(slf ,):
        print(f"TrainNo.{slf.trainNo} is running on time")

    def getFare(slf ,  fro , to):
        print(f"Ticket is booked in train number:{slf.trainNo} form {fro} to {to} fare is {randint(1 , 5555)}")
t = Train(2323)
t.book("Rampur", "Delhi")
t.getstatus()
t.getFare("Rampur", "Delhi")
