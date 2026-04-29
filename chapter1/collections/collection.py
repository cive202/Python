'''
Counter
Counter({'a': 3, 'b': 3, 'd': 3, 'c': 1})
dict_items([('a', 3), ('b', 3), ('c', 1), ('d', 3)])
dict_values([3, 3, 1, 3])

'''

from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import Counter

a = "aaabbbcddd"

my_counter = Counter(a)

print(my_counter)
print(my_counter.items())
print(my_counter.values())

'''
namedTuple
Point(x=1, y=2)
1
2

'''
Point = namedtuple(
    'Point', 'x,y')  # ==> this creates a Point Class with attributes x,y
# ==> this creates a Point instance i.e. pt with the initialization of the values x and y
pt = Point(1, 2)
print(pt)
print(pt.x)
print(pt.y)

'''
OrderDict
==> remembers the class order of which the items are appended
OrderedDict({'a': 1, 'b': 2})
'''


ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2

print(ordered_dict)


'''
defaultdict

defaultdict(<class 'str'>, {'a': 'ab', 'b': 'bc'})
'''

default = defaultdict(str)
default['a'] = 'ab'
default['b'] = 'bc'
print(default)
print(default['c'])
