#!/usr/bin/env python

from _cstruct import ffi as cs_ffi, lib as cs_lib

def c_struct(a, b, c):
    struct = cs_ffi.new("c_struct[]", 1)
    cs_lib.c_struct_init(struct, a, b, c, len(c))

if __name__ == '__main__':
    c_struct(1, b'foo', [1,3,4])
