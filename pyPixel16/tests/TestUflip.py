from unittest import TestCase
import numpy as np

import pyPixel16



class TestUflip(TestCase):

    dataUS16 = np.array(
            [0xa000, 0x7f0a, 0x0000],
            dtype=np.ushort
            ).tobytes()
    
    dataUS16flip = b"\x00\x20\x0a\xff\x00\x80"

    def testInputOuputiData(self):
        """
        Flipping dataUS16 should produce dataUS16flip.
        The raw bytes are summed to produce a sort of
        checksum.
        """
        self.assertEqual(
                sum(pyPixel16.uflip(self.dataUS16)),
                sum(self.dataUS16flip)
                )

    def testBadInputSize(self):
        """
        Cases where buffer size is not a multiple of
        the size of np.ushort should raise ValueError.
        This test sends three bytes to uflip.
        """
        with self.assertRaises(ValueError):
            pyPixel16.uflip(b"\x00\x00\x00")

    def testBadInputType(self):
        """
        Cases where buffer is not bytes type should
        raise TypeError. This test sends a unicode
        string to uflip.
        """
        with self.assertRaises(TypeError):
            pyPixel16.uflip("junk")



