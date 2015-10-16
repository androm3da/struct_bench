#!/usr/bin/env python

from __future__ import print_function

from types_ import SimpleObject, SimpleObjectImmutable, NamedTuple, SimpleTuple, c_struct
import timeit
import random

TYPES = [
    SimpleObjectImmutable,
    SimpleObject,
    NamedTuple,
    SimpleTuple,
    c_struct,
    ]

a = 1035
b = b'\x54 - fo!'
c = [1, 5, 66, ]

def measure_creation():
    random.shuffle(TYPES)

    for type_ in TYPES:
        pre = 'from __main__ import {}, a, b, c'.format(type_.__name__)
        body = '{}(a, b, c)'.format(type_.__name__)
        print('\t', type_.__name__, timeit.repeat(stmt=body, setup=pre, repeat=5))


def test_immut():
    '''Verifies that the type called SimpleObjectImmutable
       actually satisfies that definition.
    '''
    from types_ import read_only

    q = SimpleObjectImmutable(a, b, c)
    SimpleObjectImmutable.__setattr__ = read_only
    try:
        q.a = 1
        assert(False)
    except ValueError:
        assert(True)

if __name__ == '__main__':
    measure_creation()

    test_immut()
