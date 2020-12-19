# This is a test of the emergency broadcast system
import struct
from io import BytesIO

msg = b'\x02\x01\n\x00\n\x00\xb0\x00\x1a\x15\x00\x00\x00\x00]+\x01\x00\xcc\xed\xfe\xc54\x12\x00\x00\x00\x00\x00\x004\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00xV4\x12'

trace = [437, 436, 434, 434, 437, 437, 438, 435, 434, 438, 439, 437, 438,
         434, 435, 439, 438, 434, 434, 435, 437, 440, 439, 435, 437, 439,
         438, 435, 436, 436, 437, 439, 435, 433, 434, 436, 439, 441, 436,
         437, 439, 438, 438, 435, 434, 434, 438, 438, 434, 434, 437, 440,
         439, 438, 434, 436, 439, 439, 437, 436, 434, 436, 438, 437, 436,
         437, 440, 440, 439, 436, 435, 437, 501, 1122, 2358, 3509, 3816,
         3467, 2921, 2376, 1914, 1538, 1252, 1043, 877, 750, 667, 619,
         591, 563, 526, 458, 395, 403, 452, 478, 492, 498, 494, 477, 460,
         459, 462, 461, 460, 456, 452, 452, 455, 453, 446, 441, 440, 444,
         456, 459, 451, 450, 447, 445, 449, 456, 456, 455]

print(len(trace))

first_element_byte_object = b'\xB5\x01'
first_element_int_object = 437
if struct.pack('H', first_element_int_object) == first_element_byte_object:
    print("rock on")

packed_trace = b''
for element in trace:
    packed_trace += struct.pack('H', element)

with BytesIO(packed_trace) as buffer:
    while True:
        chunk = buffer.read(2)
        if chunk:
            print(struct.unpack('H', chunk)[0])
        else:
            break

buf = BytesIO(packed_trace)
with open("trc.bin", 'wb') as f:
    f.write(buf.getbuffer())
