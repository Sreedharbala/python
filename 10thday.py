#creating a set
my_set={1,2,3,4,5}
print(my_set)
# adding elements to a set
my_set.add(6)
print(my_set)

#removing an element from a set
my_set.remove(3)
print(my_set)
# set is commonly used to perform mathemativ=cal set operations like union intersection and difference they are also useful
#for eliminating duplicate elements from a list

#set operation
set1={1,2,3,4,5}
set2={4,5,6,7,8}
#output will be flower brackets{12345678}

union_set=set1.union(set2)
print(union_set)

intersection_set=set1.intersection(set2)
print(intersection_set)#{4,5}

difference_set=set1.difference(set2)
print(difference_set)#{1,2,3}

print(2 in set1)#true
print(9 in set1)#false
#in python sets are unordered collections they dont support indexing and slicing like sequences such as in lists or strings
#therefore there is not a direct method in a set however u want to reverse the eklements of a set u can convert set to a list
#reverse the list and then convert back to set

original_set={1,2,3,4,5}
print("original_set:",original_set)
# #convert set to list,reverse the list and converting back to set
#
# reversed_list=set(reversed(list(original_set)))
# print("reversed set:",reversed_list)--------waste one-------------------