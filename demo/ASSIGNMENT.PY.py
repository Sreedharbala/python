# tuple=(100,200,300,400)
# print(tuple[2])
# print(tuple[-1])
# print(tuple[-3])
#
# tuple=(300,500,400,800,600)
# tuple[4]=250
# print(tuple[4])
#
# tuple=(100,200,300,400,500)
# tuple.pop(2)
# print(tuple)
x = ("apple", "banana", "cat")
y = list(x)
y[2]="carrot"
y.append("dog")
z = ("horse",)
x = tuple(y)
x += z
(hi,*h2) = x
print(h2)
print(x)