#ordered, immutable, text representation

my_string = "Hello world \"!"
my_string2 = 'My string'#both works
my_string3 = """
Multiline
String
!!!
"""#multiline
my_string4 = """Hello \
World
!!!
"""#two lines instead of 3 because \ removes bleak
print(my_string)
print(my_string3)
print(my_string4)

char = my_string[4]#get specific element of string
subsring = my_string[1:5]#from second to 5
subsring = my_string[1:]#from second to end
subsring = my_string[:5]#from first to 5
subsring = my_string[::2]#every second
print(subsring)

newstring = my_string + " test " + subsring#concatenating
print(newstring)

for i in newstring:
    print(i)#everyletter

if "e" in newstring:#check for letter
    print("yes")
else:
    print("no")

if "llo" in newstring:#check for substring
    print("yes")
else:
    print("no")

mystring = '    Some text   '
mystring = mystring.strip()#remove white-spaces outside
print(mystring)
upperstring = mystring.upper()
lowerstring = mystring.lower()

check = mystring.startswith("some")
check = mystring.endswith("some")
print(check)

indexof = mystring.find("o")
indexof = mystring.find("me")#subsring (not fount = -1)
count1 = mystring.count("t")
print(count1)

string_with_replacement = mystring.replace('Some', 'This')
print(string_with_replacement)

my_list = my_string.split()#default delimiter is space
print(my_list)

new_string = ' '.join(my_list)
print(new_string)


name = "Tom"
age = 3
weight = 4.2021
my_string = "the name is %s" % name
my_string = "the age is %d" % age
my_string = "the weight is %f" % weight
my_string = "the weight is %.2f" % weight#2 digits after point
print(my_string)

my_string = "the variable is {}".format(name)
print(my_string)
my_string = "the variable is {:.2f} {}".format(weight,name)
print(my_string)
my_string = f"the variables is {name} and {weight:.3f}"
print(my_string)