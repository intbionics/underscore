
from src import _

a = [
    {'hello':1, 'world':1},
    {'hello':2, 'world':2},
    {'hello':1, 'world':5},
    {'hello':99, 'world':1},
    {'hello':2, 'world':6},
    {'hello':3, 'world':3},
    {'hello':4, 'world':4},
]

print(a)

print('uniq')
print(_.uniq(a, lambda x,*a: x['hello']))
print('sortBy')
print(_.sortBy(a, lambda x,*a: x['hello']))
print('max')
print(_.max(a, lambda x,*a: x['hello']))
print(_.max(range(10)))
print('min')
print(_.min(a, lambda x,*a: x['hello']))
print(_.min(range(10)))


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

a = range(100)[::-1]
print(a)
print(_.find(a, lambda i,*a: i==10))
print(_.findIndex(a, lambda i,*a: i==10))

