import binascii
from array import array

poly = 0xEDB88320

table = array('L')
for byte in range(256):
    crc = 0
    for bit in range(8):
        if (byte ^ crc) & 1:
            crc = (crc >> 1) ^ poly
        else:
            crc >>= 1
        byte >>= 1
    table.append(crc)


def crc32(string):
    value = 0xffffffff
    for ch in string:
        value = table[(ord(ch) ^ value) & 0xff] ^ (value >> 8)
    return - 1 - value

# test


data = (
    '',
    'test',
    'hello world',
    '1234',
    'A long string to test CRC32 functions',
)

for s in data:
    print(repr(s))
    a = binascii.crc32(s.encode())
    print('%08x' % (a & 0xffffffff))
    b = crc32(s)
    print('%08x' % (b & 0xffffffff))
