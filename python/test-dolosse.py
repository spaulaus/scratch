from dolosse.constants import data
from io import BytesIO
from functools import partial
from struct import unpack

header = BytesIO(b'\x2D\x40\x08\x00\x15\xCD\x5B\x07\x91\x65\x00\x00\x29\x09\x00\x00')

for chunk in iter(partial(header.read, data.WORD), b''):
    print(unpack('I', chunk)[0])
    print(unpack('I', header.read(data.WORD))[0])
    print(unpack('I', header.read(data.WORD))[0])
    print(unpack('I', header.read(data.WORD))[0])

# From HxD: 2D 40 08 00 15 CD 5B 07 91 65 00 00 29 09 00 00
