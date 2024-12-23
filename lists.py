mylist = ["banana", "cherry", "apple"]
print(mylist)

for item in mylist:
    print(item)

if "banana" in mylist:
    print("yes")
print(len(mylist))

mylist.append("lemon")#add item
mylist.insert(1, "blueberry")#add on specific possition
print(mylist)

item = mylist.pop()#remove last and return
print(mylist)

item = mylist.remove("cherry")#remove specific item
print(mylist)

mylist.clear()#remove all
print(mylist)

mylist = ["banana", "cherry", "apple"]
mylist.reverse()
print(mylist)

mylist.sort()#sort original list
newlist = sorted(mylist)#sort and return newlist
print(newlist)

mylist = [0] * 5 #new list with 5 elements = 0
print(mylist)

mylist2 = [1,2,3,4,5]
newlist = mylist + mylist2
print(newlist)#new list with 10 elements, 5 from first list 5 from second

a = newlist[3:7] #slice element from 3 to 6, last index not included
b = newlist[3:] #3 to end
c = newlist[:5] #from start to 5
d = newlist[::2] #take each second item
f = newlist[::-1] #reverse list
print(a)
print(b)
print(c)
print(d)

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org #link to list org

list_cpy = list_org.copy() #copy
list_cpy = list(list_org) #copy 2
list_cpy = list_org[:] #copy 3

print(list_cpy)

a = [1,2,3,4,5,6]
b = [i*i for i in a] #for loop to create new list

print(a)
print(b)