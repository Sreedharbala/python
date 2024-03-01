
# listname=[1,2,3,4]
# print(listname)
favfruits=["apple","mango","PAppaya"]
# print(favfruits)
print(favfruits[1])
favfruits[1]="orange"
print(favfruits)
favfruits.append("kiwi")# add the object at end of the object
favfruits.append("onion")
print(favfruits[3])
favfruits.insert(1,"dragon fruit")
# insert object in the given index
print(favfruits)
favfruits.remove("apple")
# for removing the object
print(favfruits)

favfruits.sort()
# sorting objects in order  first they take capital and small letters and again numbers
print(favfruits)

favfruits.reverse()
# it reverse the objects
print(favfruits)

favfruits.pop()
# it used to remove last index value or given index value
print(favfruits.pop())

wardates=(1945,1962)
#  tuple having the() brackets

print(wardates)


camera={"sony":600,"nikon":650,"canon":650}
print(camera)
# FOR UPDATING THE VALUES IN THIS
camera["nikon"]=500
print(camera)

favfruit={"ant","buffalo","dog","kite"}
print(favfruit)
favfruit.pop()
print(favfruit.pop())
