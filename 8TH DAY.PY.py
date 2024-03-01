#lambda function
# Add=lambda x:x+45
# result=Add(20)
# print(result)

# Add=lambda x,y:x+y
# result=Add(20,30)
# #print(result) and also by below type
# print(Add(20,35))
# lambda functions are best used where u need a small one off funnction for a short
# period of time especially when u dont want to define a full fledged function using the def keyword
#passing functions as arguments simple transformations,anonymous functions and call back function
#lambda fun are not suitable for complex logics and or large block of code


#how to use a lambda function inside userdefined function

def classroom(n):
    square = lambda x : x + n
    return square
demo = classroom(20)
print(demo(40))

# def multiplier(n):
#     multiply = lambda x : x * n
#
#     return multiply
# multiplier_by_5=multiplier(5)
# print(multiplier_by_5(10))
# print(multiplier_by_5(20))

#modules
#packages are collection of modules

