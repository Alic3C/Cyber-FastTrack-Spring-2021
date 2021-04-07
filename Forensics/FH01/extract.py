#!/usr/bin/env python3

import struct

OP_PKT_SEGMENT = 2048

def to_bytes(s):
    b = []
    i = 0
    while i < len(s):
        b.append(int(s[i:i+2], 16))
        i += 2

    return bytes(b)


curr_file = 1
curr_segment = 1
curr_data = bytearray()

with open('extracted.dmp', 'r') as f:
    for line in f:
        data = to_bytes(line.strip())

        pkt_id, pkt_op = struct.unpack('<QQ', data[:16])

        if pkt_id == curr_segment:
            if pkt_op == OP_PKT_SEGMENT:
                if curr_segment == 1:
                    print('New segment detected.')

                curr_data.extend(data[16:])
                curr_segment += 1
            else:
                print(f'Got op code {pkt_op}, assuming we are done with this file.')
                curr_data.extend(data[16:])
                with open(f'{curr_file}.bin', 'wb') as out:
                    out.write(curr_data)

                curr_file += 1
                curr_segment = 1
                curr_data = bytearray()
        else:
            print(f'Out of order segment found, expected {curr_segment}, got {pkt_id}')

