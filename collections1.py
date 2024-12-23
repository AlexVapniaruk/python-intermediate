#counter, namedtuple, OrderedDict, default dict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
a = "aaaabbbccc"

my_counter = Counter(a)
print(my_counter)#Counter({'a': 3, 'b': 3})
print(my_counter.most_common(1))#[('a', 4)] list with tuples
print(list(my_counter.elements()))#['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)#Point(x=1, y=-4)
print(pt.x)
print(pt.y)

orderred_dict = OrderedDict()
orderred_dict['a'] = 1
orderred_dict['c'] = 3
orderred_dict['d'] = 4
orderred_dict['b'] = 2
print(orderred_dict)#OrderedDict({'a': 1, 'c': 3, 'd': 4, 'b': 2})
#can be replaces with {} regualr dictionary that remember order from python 3.7

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])#return default value for int = 0

deck1 = deque()

deck1.append(1)
deck1.append(2)
deck1.appendleft(3)
print(deck1)#deque([3, 1, 2]
deck1.pop()
deck1.popleft()
print(deck1)#deque([1])
deck1.clear()
deck1.extend([4,5,6])
deck1.extendleft([9,7,8])
print(deck1)#deque([8, 7, 9, 4, 5, 6])
deck1.rotate(1)
print(deck1)#deque([6, 8, 7, 9, 4, 5])
deck1.rotate(2)
print(deck1)#deque([4, 5, 6, 8, 7, 9])
deck1.rotate(-1)
print(deck1)#deque([5, 6, 8, 7, 9, 4])