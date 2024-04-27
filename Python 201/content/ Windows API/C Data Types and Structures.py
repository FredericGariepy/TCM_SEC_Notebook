# Mostly described by the MSDN (Microsoft Developer Network)
#https://docs.python.org/3/library/ctypes.html
from ctypes import *

b0 = c_bool(0)

print(b0)
print(type(b0))
print(b0.value)

i0 = c_uint(-1)
print(i0.value)
i1 =  c_uint(100)
print(i1.value)

c0 = c_char_p(b"test")
print(c0.value)

p0 = create_string_buffer(5)
print(p0)
print(p0.raw)
print(p0.value)

p0.value = b'a'
print(p0.raw)

#pointers
l0 = c_int(42)
pl0 = pointer(l0)

print(l0)
print(pl0)
print(type(l0))
print(type(pl0))
print(pl0.contents)

print(hex(addressof(l0)))

pt =  byref(p0)
print(pt)

print(cast(pt, c_char_p).value)

print(cast(pt, POINTER(c_int)).contents)
print(ord('a'))

# Struct

class PERSON(Structure):
    _fields_ = [("name", c_char_p),("age", c_int)]

hacker =  PERSON(b'fred',30)
print(hacker.name)
print(hacker.age)

person_array_t = PERSON * 3
print(person_array_t)
person_array =  person_array_t()
print(person_array)
person_array[0] = hacker
person_array[1] = PERSON(b'bob',50)
person_array[2] = PERSON(b'alice', 60)

"""
c_bool(False)
<class 'ctypes.c_bool'>
False
4294967295
100
b'test'
<ctypes.c_char_Array_5 object at 0x7ff22e7710c0>
b'\x00\x00\x00\x00\x00'
b''
b'a\x00\x00\x00\x00'
c_int(42)
<__main__.LP_c_int object at 0x7ff22e7711c0>
<class 'ctypes.c_int'>
<class '__main__.LP_c_int'>
c_int(42)
0x7ff22e771190
<cparam 'P' (0x7ff22e771110)>
b'a'
c_int(97)
97
b'fred'
30
<class '__main__.PERSON_Array_3'>
<__main__.PERSON_Array_3 object at 0x7ff22e771240>
"""
