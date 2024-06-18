# #appending the string
#
# string = "sreedhar 'is'"
# print(string)
#
# print(string.upper())
# print(string.replace("is","balu"))
#
# #list
# list = [1,2,4,8,5,8]
# list.append(10)
# print(list)
# list.sort()
# print(list)
# list.remove(5)
# print(list)
# list.reverse()
# print(list)
# list.count(5)
# print(list)
# list1 = [21,22,23,24,25]
# list.extend(list1)
# print(list)
# list1 = ("hi","bye")
# list.extend(list1)
# print(list)
#
# squares = [x**2  for x in range(1,20)]
# squares1 = [j**3 for j in range(1,10)]
# print(squares1)
# print(squares)
#
# evens = [k for k in range(1,20)if k%2==0 ]
# odd = [k for k in range(1,20)if k%2==1 ]
# print(evens)
# print(odd)
#
# string = "hello, world "
# chars =  [m for m in string if m.isalpha()]
# print (chars)
#
# string = "word having length"
# word_length = [len(word) for word in string.split()]
# print(word_length)
#
# generate a list of tuples containing a number and it's square
# list = [(x,x**3) for x in range (1,10)]
# tuples = [x**2 for x in list]
# print(list)

# a = [x for x in range(1,20) if x%2==0]
# print(a)


# lowercase_letters = [chr(x) for x in range(ord('a'),ord('n')+1)]
# print(lowercase_letters)
#
# uppercase_letters = [chr(x) for x in range(ord('A'),ord('Z')+1)]
# print(uppercase_letters)
#
# even_square = [(x,x**2) for x in range(1,11) if x%2==0]
# print(even_square)
# odd_cube = [(f,f**3) for f in range(1,11) if f%2==1]
# print(odd_cube)
#
# result = [s**2 if s%2==0 else s**3 for  s in range(1,11)]
# print(result)
#
# c_multiple = [x for x in range(1,101) if x%3==0 and x%5==0 ]
# print(c_multiple)
#
# words = ["apple","banana","cat"]
# reversed_words = [word[::-1] for word in words]
# print(words)
# print(reversed_words)


# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n % i==0:
#             return False
#     return True
#
# prime_numbers = [x for x in range(1,51) if is_prime(x)]
# print(prime_numbers)

# squares = [x**2 if x%2==0 else x**3 for x in range(-5,5)]
# print(squares)

# functions
# def function():
#     print("this is a function statement")
#
# function()

# def function(num1,num2):
#     num3 = num1 + num2
#     return num3
# # num1,num2 = 5,15
# ans = function(5,15)
# print(f"the addition of {5} and {15} results {ans}.")
# def is_prime(n):
#     if n in [2, 3]:
#         return True
#     if (n == 1) or (n % 2 == 0):
#         return False
#     r = 3
#     while r * r <= n:
#         if n % r == 0:
#             return False
#         r += 2
#     return True
# print(is_prime(78), is_prime(79))


# def student(firstname,lastname):
#     print(firstname,lastname)
# student("sreedhar","")
# student("","bala")

# def function(**name):
#     print(list(name))
#     print(set(name))
#     print(name)
#
# function(name="sree",neme="bala",heli="hello")

#nested funnction
# def a1():
#     b = "hello world"
#     def a2():
#         print(b)
#     a2()
# a1()

# def factorial(a):
#     if a == 0:
#         return 1
#     else:
#         return a * factorial(a-1)
# print(factorial(4))
#pass by value by reference
# def function(x,y):
#     x[0]=30
#     y[1] = "R"
#
# st = [10,11,12,13,14,15]
# y = ["bala","sree","hello"]
# function(st,y)
# print(st,y)
# only index will change

# function swap
# def swap(x,y):
#     temp = x
#     x = y
#     y = temp
#
# x = 2
# y = 3
# swap(x,y)
# print(x)
# print(y)

# def cube(x):
#     return x*x*x
#
# cube_v2 = lambda x : x*x*x
# print(cube(8))
# print(cube_v2(9))


# import firstprogram as bro
# bro.greetings("sreedhar")

class parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printer(self):
        print(self.name,self.age)
class child(parent):
   def __init__(self,name,age,year):
       super(). __init__(name,age)
       self.year = year
   def print(self):
       print("hello",self.name,  "welcome", self.age, "year", self.year)

one = child("sree",25,2025)
one.printer()
one.print()

