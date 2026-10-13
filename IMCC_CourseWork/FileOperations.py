#file operations 
#read file 
f= open("myfiles.txt")
print(f.read())
f.close()


with open("myfile.txt") as f:
    print(f.read(6))
    ct= f.read()
    ws = ct.split()
    print("tot characgter",ct)
    print("tot words are", len(ws))


#line by line reading

with open("myfile.txt") as f:
    l1=f.readline()
    l2=f.readline()
print(l1,l2)

#reading file without readline

with open("myfile.txt") as f:
    print("output using for")
    for i in f:
        print(i)


with open("myfile.txt","r") as f:
    print("\noutput using readlines which reads complete filr \n")
    txt=f.readline()
f.close()


with open("myfile.txt") as f:
    f.write(" \n newly added content")

