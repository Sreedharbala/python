#11th day oops
#class
 #classes=classes are userdefined blue print or prototype
#eg:if calci is class then sum,multiplication and subraction will be methods
#so classes will consists of methods class variables,instance variables and constructor etc
#> creation of new object not needed ex in java we will create new to create object

# class calculator:
#     num=100
#     def __init__(self,a,b):
#         self.firstnumber = a
#         self.secondnumber = b
#         print('i am called automatically when object is created')
#     def getdata(self):
#         print("i am now executing as method in class")
#     def summation(self):
#         return self.firstnumber + self.secondnumber+calculator.num
# obj = calculator(40,20)
# obj.getdata()
# print(obj.num)
# print(obj.summation())

#again 12 th day start here
# obj1 = calculator()
# obj1.getdata()
#constructor is a method when object is created constructor is first one to call
#self is used as a reference to the current instance of a class whe you define methods with in a class
#you must include self as the first parameter in the method definition.
#self keyword is mandatory for calling variable names into method.constructor name should be
#'__name__' when creating.,new keyword does not required for object.

#again 12 th day start here

class python:
     num=350
     num3=120
     num5=350
     def __init__(self):
      self.firstnumber=450
      self.secondnumber=550
      print(self.firstnumber+self.secondnumber)

     def python1(self):
       return self.firstnumber*self.secondnumber+self.num+self.num3+self.num5



# obj= python()
# print(obj.python1())


class First(python):
    value=500
    value2=300
    value3=600
    # def __init__(self):
    #     pass
    def first1(self):
        print(self.value*self.value2+self.value3)
        print(self.firstnumber+self.secondnumber)

first=First()
first.first1()
print(first.value3)




