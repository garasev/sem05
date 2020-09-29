import sys
import struct
import ctypes
obj = 1
list = [9, 8, 7, 5]
for i, a in enumerate(list):
    print(i, a)
print(sys.getsizeof(obj), obj.__sizeof__())
print(struct.unpack('LLl', ctypes.string_at(id(obj), 12)))
obj2 = obj
print(struct.unpack('LLl', ctypes.string_at(id(obj2), 12)))
obj3 = 2
print(struct.unpack('LLl', ctypes.string_at(id(obj3), 12)))