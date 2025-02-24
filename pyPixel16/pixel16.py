#/usr/bin/env python3

import numpy as np

__all__ = [
        "byteswap", 
        "uflip",
        ]

def uflip(image):
    a = np.frombuffer(image, dtype=np.ushort)
    a = __do_uflip(a)
    return a.tobytes()


def byteswap(image):
    a = np.frombuffer(image, dtype=np.ushort)
    a = __do_byteswap(a)
    return a.tobytes()


def __do_uflip(a):
    return np.bitwise_xor(a, 0x8000)


def __do_byteswap(a):
    return a.byteswap()
