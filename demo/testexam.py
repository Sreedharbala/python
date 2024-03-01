#1.question
import math

list=[0,2,3,4,10,25,12]
list.append(5)
print(list)


list.remove(3)
print(list)

list.sort()
print(list)

list.reverse()
print(list)

#2nd question
list=[1,2,3,4,5,6,7,8,10]
square=math.sqrt(list[2])
print(square)


#3rd question
lista=[101,102,103,104,105,106]
listB=[107,108,109,110,111]
lista.append(listB)
print(lista)

#4th question

tuple = ("apple","ball","cat","dog","eye")
print(tuple)

tuple1 = (21,20,25,22,25,24)
tuple1.count(1)
print(tuple1)


value = (30,33,31,35,34,32)



dictionary={"ramesh":56,"suresh":57,"bhanu":58,"dinesh":59}
dictionary1=dictionary.copy()
dictionary["ramesh"]=102
print(dictionary1)
print(dictionary)

dict ={"ramesh":56,"suresh":57,"bhanu":58,"dinesh":59}
dict1={"ramesh":56,"suresh":57,"bhanu":58,"dinesh":59}
dict.sort
print(dict)




word = 25

try:

    word3 = 0
    word/word3
except NameError:
    print("the name is not defined")
except ZeroDivisionError:
    print("the word is not divisible by zero")
except Exception:
    print("there is  error")
finally:
    print("finally executed")
