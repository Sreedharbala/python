#matrix
# number=1
# for row in range(1,4):
#     for column in range(1,):
#         print(number)
#         number=number+1
#     print()
#exception handling
length=0
width=45
length/width
try:

    width=4
    length/width
except Exception:
    print("have caught a new error")
except NameError:
    print("variable has to be used before defining it")
except ZeroDivisionError:
    print("division by zero is not valid!kindly change your input")
# except Exception:
#     print("have caught a new error")

finally:
    print("finally block executed")

# number=0
# for row in range(1,3):
#     for column in range(1,4):
#         print(number,end=' ')
#         number=number+1
#     print()
