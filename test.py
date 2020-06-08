
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

