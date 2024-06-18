from abc import ABCMeta,abstractmethod


class A(metaclass=ABCMeta):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

    @abstractmethod
    def method3(self):
        pass

    @abstractmethod
    def method4(self):
        pass
class B(A):
    def method1(self,name):
        self.name = "name"
        print(name)


    def method2(self,lastname):
        self.lastname= "bala"

    def method3(self,education):
        self.education= "btech"

    def method4(self,branch):
        self.branch = "civil"

class C(A):
    def method1(self,name):
        self.name = "name"
        print(name)


    def method2(self,lastname):
        self.lastname= "bala"

    def method3(self,education):
        self.education= "btech"

    def method4(self,branch):
        self.branch = "civil"

Obj1 = B()
Obj1.method1("sreedhar")

Obj2 = C()
Obj2.method1("anand")
