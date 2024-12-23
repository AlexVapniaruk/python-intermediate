#key-value pairs, unordered, mutable
#key - number, string, tuple (because its can be hashed)
mydict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}
print(mydict)

mydict2 = dict(name="Mary", age="27", city="New York")
print(mydict2)

value = mydict2["name"] #get value for key
mydict2["email"] = "alex@alex.com" #set signle key-value

del mydict2["name"] #delete key-value pair
mydict2.pop("age") #delete key-value pair
mydict2.popitem() #delete key-value pair last one

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict2["name"])
except:
    print("Error")


for key in mydict:
    print(key)

for key in mydict.keys():#same ^
    print(key)

for key in mydict.values():
    print(key)

for key, value in mydict.items():#key-value
    print(key, value)

mydict_link = mydict

print(mydict_link) #same as original, if modify original, modified linked

mydict1_copy = mydict.copy() #real copy

mydict2_copy = dict(mydict) #copy as well


mydict.update(mydict2) #merge 2 dictionaries, existing overwritten, non existing added
print(mydict)

mytuple = (8, 7)

mydict = {mytuple: 15}#key as a tuple

print(mydict) 