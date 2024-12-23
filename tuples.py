#Tuple - cannot be changed after it created (immutable)
# tuples take less memory that lists
# to create tuple take less time that list
mytuple = ("Max", 28, "Boston")
mytuple2 = "Max", 28, "Boston" #both valid
mytuple3 = tuple(["Max", 28, "Boston"])#create tuple from list
print(mytuple)

myt = ("Max") #not Tuple, type String
myt2 = ("Max",) #Tuple

item = mytuple[0]
print(item)

if "Max" in mytuple:
    print("yes")

print(len(mytuple))

newtuple = ("a", "p", "p", "l", "e")
print(newtuple.count("p"))
print(newtuple.index("a"))

#convert tuple to list and back
mylist = list(newtuple)
mytuplelist = tuple(mylist)

a = newtuple[0:2] #same like with lists

name, age, city = mytuple #unpacking into variables
print(name)
print(age)
print(city)

i1, *i2, i3 = newtuple
print(i1)#a
print(i2)#['p','p','l']
print(i3)#e