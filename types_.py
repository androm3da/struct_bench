#!/usr/bin/env python

import collections

def read_only(self, name, val):
    raise ValueError('not supported')


class SimpleObject(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.b = c

class SimpleObjectImmutable(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.b = c


NamedTuple = collections.namedtuple('NamedTuple', ['a', 'b', 'c',])

def SimpleTuple(a, b, c): return (a, b, c)

from types_c import c_struct
