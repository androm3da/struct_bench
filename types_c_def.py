
from cffi import FFI

ffi = FFI()
ffi.cdef("""
    typedef struct {
        int a;
        char b[128];
        int c[128];
    } c_struct;
    int c_struct_init(c_struct *entry, int a, const char *b, const int *c, int c_elems);
""")

ffi.set_source("_cstruct",
"""
    typedef struct {
        int a;
        char b[128];
        int c[128];
    } c_struct;
    int c_struct_init(c_struct *entry, int a, const char *b, const int *c, int c_elems)
    {
        return 0;
    }
""")


if __name__ == '__main__':
    ffi.compile()
