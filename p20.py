mylist=["Oil","Soap",123,"Oil","Kurkure","Dairy-milk"]
print(mylist)
print(type(mylist))
print(mylist[0])

# slicing list method
print(mylist[1:1])
print(mylist[2:5])

#you can use negative index as well
print(mylist[-1])
print(mylist[-2])
for i in mylist:
    print(i,end="")
