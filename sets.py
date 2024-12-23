#unordered, mutable, no duplicates

myset = {1, 4, 6, 1, 2}
print(myset)#result {1,2,4,6}

myset = set([1,2,3]) #from list
print(myset)

myset = set("Hello")
print(myset)

myset = {}
print(type(myset))#dictionary!!
myset = set()
print(type(myset))#set

myset.add(5)
myset.add(3)
myset.add(9)
myset.add(7)

print(myset)

myset.remove(3)
#myset.remove(4) #ERROR, not exist
myset.discard(4)#No error delete
print(myset)

print(myset.pop())#return and remove first

myset.clear()#remove all

myset.add(5)
myset.add(3)
myset.add(9)
myset.add(7)

for x in myset:
    print(x)

if 1 in myset:
    print("yes")
else:
    print("no")



odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

union1 = odds.union(evens)#merge without duplication, union of both
print(union1)

intersection1 = odds.intersection(primes) #numbers that in both sets / перетин
print(intersection1)

difference1 = union1.difference(intersection1) #all from first that NOT in second
print(difference1)

symmetric_difference1 = evens.symmetric_difference(primes)#all from first and second, but without numbers that in both sets
print(symmetric_difference1)

odds.update(evens)#update original odds, merge, without creation new set
odds.intersection_update(evens)#only element that found in both
odds.difference_update(evens)#remove from set 1 element fount in set 2
odds.symmetric_difference(evens)#remove elements that found in both


print(evens.issubset(odds)) #check if set 1 in fully in other set 2, if odds has events(fully)
print(evens.issuperset(odds)) #check if set 1 is contain set 2, if event has odds(fully)
print(evens.isdisjoint(odds)) #check if set 1 do not have any elements from set 2

setA = {1, 2, 3, 4, 5, 6}

setB = setA #linking
print(setB)

setB = setA.copy()#real copy
setB = set(setA) #real copy as well

a = frozenset([1,2,3,4])#immutable

a.add(5)#error because set frozen

print(a)