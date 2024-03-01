#hover _ riding
class Employee:
    def setnoofworkinghours(self):
        self.numberofworkinghours=40

    def displaythenoofworkinghours(self):
        print(self.numberofworkinghours)

    # def thirdmethod(self):
    #     print("it will be taken from first class")

class Trainee(Employee):
    def setnoofworkinghours(self):
        self.numberofworkinghours=45

    def resetnoofworkinghours(self):
        super().setnoofworkinghours()


employee = Employee()
employee.setnoofworkinghours()
print("number of working hours of employees:", end = "")
employee.displaythenoofworkinghours()

trainee = Trainee()
trainee.setnoofworkinghours()
print("number of working of trainee:", end = " ")
trainee.displaythenoofworkinghours()
# trainee.thirdmethod()
trainee.resetnoofworkinghours()
print("no of working hours has been reset:", end="")
trainee.displaythenoofworkinghours()

