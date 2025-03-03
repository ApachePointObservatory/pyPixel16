# pyPixel16

Author: Gordon A. MacDonald, PhD, Apache Point Observatory, NM

This is a collection of functions that perform bit- and bitewise operations of byte strings of unsigned shorts (16-bits on most systems). It performs the operations using Numpy. This package will replace the [pixel16](https://github.com/ApachePointObservatory/pixel16.git) wrapper (author unknown).

1. ```uflip```: flips the most significant bits in a string of unsigned short ints.
2. ```byteswap```: swaps bytes in a string of unsigned short ints.

Beware that any byte string will always be interpreted as a string of 16-bit unsigned ints (unsigned short). If the original bytes were derived from char, int32, or anything else, these will be read-in and processed as if they were unsigned shorts.

## Installation

```
python3 -m build
pip3 install build/pyPixel16-0.0.1.whl
```

## How to use pyPixel16

Below is a code snippet demonstrating the use of pyPixel16 in the interpreter.

```
>>> import pyPixel16
>>> pyPixel16.byteswap(b"abcd")
b'badc'
>>> pyPixel16.uflip(b"\x00\xff\x07\x80")
b'\x00\x7f\x07\x00'
>>> pyPixel16.uflip(b"\x00\xff\x07\x80\x01") ## Input must have an even-number of bytes.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/gmac/Documents/dev/pyPixel16/pyPixel16/pixel16.py", line 48, in uflip
    a = np.frombuffer(b, dtype=np.ushort)
ValueError: buffer size must be a multiple of element size
>>> pyPixel16.uflip("abcd")	## Input must be bytes-like
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/gmac/Documents/dev/pyPixel16/pyPixel16/pixel16.py", line 48, in uflip
    a = np.frombuffer(b, dtype=np.ushort)
TypeError: a bytes-like object is required, not 'str'
```
