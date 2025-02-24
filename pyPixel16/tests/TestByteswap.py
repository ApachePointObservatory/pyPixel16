import unittest
import numpy as np

import pyPixel16



class TestByteswap(unittest.TestCase):

    dataUS16 = np.array(
            [0xf000, 0x7f0a, 0x0000],
            dtype=np.ushort
            ).tobytes()

    dataUS16flip = b"\xf0\x00\x7f\x0a\x00\x00"

    def testInputOuputiData(self):
        """
        Swapping bytes in dataUS16 should produce
        dataUS16flip.
        """
        self.assertEqual(
                pyPixel16.byteswap(self.dataUS16),
                self.dataUS16flip
                )

    def testBadInputSize(self):
        """
        Cases where buffer size is not a multiple of
        the size of np.ushort should raise ValueError.
        This test sends three bytes to byteswap.
        """
        with self.assertRaises(ValueError):
            pyPixel16.byteswap(b"\x00\x00\x00")

    def testBadInputType(self):
        """
        Cases where buffer is not bytes type should
        raise TypeError. This test sends a unicode
        string to byteswap.
        """
        with self.assertRaises(TypeError):
            pyPixel16.byteswap("junk")

