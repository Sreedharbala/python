from classdemo import calculator

class childimpl(calculator):
    num2=200

    def __init__(self):
        calculator.__init__(self,2,10)
    def getcompletedata(self):
        return self.num2 + self.num + self.summation()

obj=childimpl()
print(obj.getcompletedata())



#input()
print("hello world")
print("what is your name")
myname=input()
print("it\'s good to meet you:"+myname)
print("the length of your namr is: ",len(myname))
print("what is your age?")
myage=input()
print("you will be"+str(int(myage)+1)+"in a year")



