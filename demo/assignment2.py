#first program:
# number=int(input("enter number:"))
# if number>=0:
#     print("the number is positive")
# elif number<=0:
#     print("the number is negative")
# else:
#     print("zero")

#second program:
# year=int(input("enter year:"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("{} is a leap year".format(year))
#         else:
#             print("{} is not a leap year".format(year))
#     else:
#         print("{} is a leap year".format(year))
# else:
#     print("{} is not a leap year".format(year))
#
# def checkyear(year):
#     return((year % 4 == 0) and(year % 100!=0) or(year % 400==0))
# year=2000
# if (checkyear(year)):
#     print("leap year")
# else:
#     print("is not a leap year")

#third program
# a=int(input("first number:"))
# b=int(input("second number:"))
# c=int(input("third number:"))
# if(a>b and a>c):
#     print(f"the maximum value is:{a}")
# elif(b>a and b>c):
#     print("the maximum value is:{}".format(b))
# elif(c>a and c>b):
#     print("the maximum value is:{}".format(c))
# else:
#     print("enter the values in different ways")



# num1=14
# num2=25
# num3=20
#
# if(num1>=num2) and (num1>=num3):
#     value=num1
# elif(num2>=num1) and (num2>=num3):
#     value=num2
# else:
#     value=num3
#
# print("the largest number is:",value)

#4th program
# s=input("enter the string or value:")
# reverse=s[::-1]
# if(s==reverse):
#     print("this is a palindrome")
# else:
#     print("this is not a palindrome")

#5th program
# age=int(input("enter age:"))
# if(age<=12):
#     print("child")
# elif(age==13 and age<=19):
#     print("teenager")
# elif(age>20 and age<60):
#     print("adult")
# elif(age>60):
#     print("senior")
# else:
#     print("enter integer values")

#6th program
# a=int(input(" a value:"))
# b=int(input("b value:"))
# c=int(input("c value:"))
#
# s=(a+b+c)/2
#
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print("area of triangle is %0.2f" %area)

#7Develop a Python program that takes a user's score as input and prints
# their grade according to the following
# scheme: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59).

# score=int(input("score:"))
# if(score>=90):
#     print("A grade")
# elif(score>=80):
#     print("B grade")
# elif(score>=70):
#     print("C grade")
# elif(score>=60):
#     print("D grade")
# elif(score<=59):
#     print("failed exam")
# else:
#     print("enter integer values")

#


# class Demo:
#      num=12
#
#      # def __init__(self):
#      #     self.num2=5
#
#      def demo2(self):
#          print( self.num)
#      def demo3(self):
#          print(self.demo2())
#
#
#
# DEMO = Demo()
# DEMO.demo2()
# DEMO.demo3()

# student = {"anitha","bhavana","charan","dinesh"}
# marks = student
# print(marks)

students = {"harsha": (30, 60, 80, 50, 50), "sajith": (50, 60, 40, 90, 80)}
for i, j in students.items():
    score = 0
    for a in j:
        score += a
    print(i, score)