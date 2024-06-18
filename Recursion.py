# it is programming technique where a function call itself in order to solve a program
def factorial(n):
    if n==0 or n==1:
        return 1
    #recursive case
    else:
        return  n * factorial(n-1)
print("Factorial of 5 :",factorial(5))

# def countdown(n):
#     if n<=0:
#         print("lift off")
#     else:
#         print(n)
#         countdown(n-1)
#example usage
# countdown(10)


def fibonacci(n):
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0

    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))




