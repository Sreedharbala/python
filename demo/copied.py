import copy
original_dict = {'a':1,'b':{'c':2, 'd':3}}
#shallowcopy
shallow_copied_dict = copy.copy(original_dict)
#deep copy
deep_copied_dict = copy.deepcopy(original_dict)
#modified the nested dictionary in the shallow copy
shallow_copied_dict['b']['c'] = 100
#modified the nested dictionary in the deep copy
deep_copied_dict['b']['d'] = 100
# Print the original dictionary and the copied dictionaries
print("Original Dictionary:", original_dict)
print("Shallow Copied Dictionary:", shallow_copied_dict)
print("Deep Copied Dictionary:", deep_copied_dict)