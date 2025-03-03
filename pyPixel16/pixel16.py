#/usr/bin/env python3

import numpy as np

__all__ = [
        "byteswap", 
        "uflip",
        ]

def uflip(b):
    """
    Flips the most significant bit of an unsigned short, b
    by performing the bitwise XOR b ^ 0x8000.

    Parameters
    ----------
        bytes-like 
            A string of an even number of bytes.
            This string will be interpreted
            as a string of 16-bit unsigned int
            (i.e. unisgned short).

    Returns
    -------
        bytes
            A string of an even number of bytes
            with the most significant bit of each
            16-bit byte pair flipped.

    Raises
    ------
        TypeError
            b is not bytes-like.

        ValueError
            b holds an odd number of bytes.

    Examples
    --------
        >>> pyPixel16.uflip(b"\\x00\\x8f\\xff\\x70")
        b'\\x00\\x0f\\xff\\xf0'

        First byte unchanged
        Second byte flipped from 0x80 to 0x00
        Third byte unchanged
        Fourth byte flipped 0x70 to 0xf0
    """
    a = np.frombuffer(b, dtype=np.ushort)
    a = __do_uflip(a)
    return a.tobytes()


def byteswap(b):
    """
    Swaps bytes of an unsigned short int.

    Parameters
    ----------
        b : bytes-like:
            A string of an even number of bytes.
            This string will be interpreted
            as a string of 16-bit unsigned int
            (i.e. unsigned short).

    Returns
    -------
        bytes
            A string of an even number of bytes
            with byte order swapped.

    Raises
    ------
        TypeError
            b is not bytes-like.

        ValueError
            b holds an odd number of bytes.

    Examples
    --------
        >>> pyPixel16.byteswap(b"\\x00\\x8f\\xff\\x70")
        b'\\x8f\\x00p\\xff'

        The byte order of the first + second bytes
        and the third + fourth bytes are swapped. Note
        \\x70 is encoded as char 'p'.
    """
    a = np.frombuffer(b, dtype=np.ushort)
    a = __do_byteswap(a)
    return a.tobytes()


def __do_uflip(a):
    return np.bitwise_xor(a, 0x8000)


def __do_byteswap(a):
    return a.byteswap()
