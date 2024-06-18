#open the file in read mode ('r')
#file input and file output


with open('C://Users//Lenovo//Desktop//hello world.txt','r') as f:
    #read all the lines in the list


    lines = f.readlines()
for line in lines:
    print(line.strip())#remove the new linecharacter at the end of new line


# #open the file in write mode('w')
#
with open('C://Users//Lenovo//Desktop//hello world.txt','w') as f:

    f.write("hi there have a great day.\n")
    f.write("python is great language.\n")
    f.write("future of ai.\n")
print("data is written in hello world.txt")
#
#
with open('C://Users//Lenovo//Desktop//hello world.txt','a') as f:

    f.write("hi there have a great day.\n")
    f.write("python is great language.\n")
    f.write("future of ai.\n")
print("data is append in hello world.txt")
f.close()
