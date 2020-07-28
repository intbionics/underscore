
from src import _

a = [
    {'hello':1, 'world':1},
    {'hello':2, 'world':2},
    {'hello':1, 'world':5},
    {'hello':2, 'world':6},
    {'hello':3, 'world':3},
    {'hello':4, 'world':4},
]

print(a)

b = _.uniq(a, False, lambda x,*a: x['hello'])

print(b)

class Obj1(object):
    a = 1
    b = 2
    c = {'d':'d'}
    d = 4

o1 = Obj1
print(_.get(o1,'a'))
print(_.get(o1,'b'))
print(_.get(o1,'c'))
print(_.get(o1,'c.d'))
print(_.get(o1,'d'))
print(_.get(o1,'e'))



