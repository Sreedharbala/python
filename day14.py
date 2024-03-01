# day14 feb07
# method overriding refer to the ability of a subclass to provide  a specific implementation of a method that is defined
# in itis superclass.
#  when method in sub class has the same name, parameters and return typs as method in its superclass
# the method in the subclass overrides the method in the superclass
#diamond problem


class A:
    def method(self):
        print("method of class A")
class B(A):
    # pass
     def method(self):
         print("method of class B")
class C(B):
    #pass
     def method(self):
          print("method of class C")
class D(C,B,A):
         pass

d=D()
d.method()

#return= is used inside a function to exit the function and return a value back to the caller
#it is typically the last statement in the function although you can have multiple return statements in
#different parts of the function.

#pass is a null operation in pyhton it is used as a placeholder in a function when a statement is syntatically required
# it is typically used syntax ,but you dont need any action to be taken

#polymorphism in pyhton refers to the ability of different objects to respond to the same method or function
#called in different ways it allows objects of different classes to be treated as objects of a common super class.
#duck-typing:is concept in pyhton where the type or class of an object is less importance then the method its defined.
