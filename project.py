# from tkinter import *
# master = Tk()
# def callback():
#     print("you clicked the button")
#
#
# btn = Button(master, text="ok",command = callback())
# btn.pack()
# mainloop()
import random

#BANK

# def function():
#     print("enter 1 to create new account"
#           "enter 2 to oopen existing account"
#           "enter 3 to exit ")
#     a=int(input())
#     if(a==1):
#         print("enter your name:")
#         b = input()
#         print("your first deposit")
#
# function()
print("enter 1 to create a new account")
print("enter 2 to open an existing account")
print("enter 3 to exit")
a = int(input());
if a==1:
    print("enter your name:")
    str(input())
    print("enter your first deposit amount:")
    int(input())
    print("your account no is:",random.randint(100000,999999))
    b = int(input())
    if b==2:
        print("Enter your name:")
        str(input())
        print("Enter your account number")
        int(input())
        print("Authentication successful")
    elif b == 3:
        print("")
elif a==2:
    print("enter your name")
    str(input())
    print("Enter your account number:")
    int(input())
    print("Authentication successful")
elif a==3:
    print("")
    # else:
    #     print("enter something")
# class BankAccount :
#     def __init__(self,enter):
#         self.enter = "enter your name:";
#
#
#     def printing(self):
#         print(self.enter)
#
#
# o1 = BankAccount(input(if(self.enter=1):
#     print(o1.printing())));




