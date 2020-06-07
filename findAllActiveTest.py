import unittest
import StringIO
from findAllActive import *

class TestFindAllActiveMethods(unittest.TestCase):
    def test_isContainsAttackBox_returnsTrue(self):
        jonbin = """
        JONBx00\x01\x00jn000_05.bmp12345678901234567890\x14\x010003
        """
        buf = StringIO.StringIO(jonbin)
        isContainsAttackBox(buf)

    def test_isContainsAttackBox_returnsFalse(self):
        jonbin = """
        JONBx00\x01\x00jn000_05.bmp12345678901234567890\x14\x010000
        """
        buf = StringIO.StringIO(jonbin)
        isContainsAttackBox(buf)

    def test_isContainsAttackBox_returnsTrue_whenThereAre2sprites(self):
        jonbin = """
        JONBx00\x02\x00jn000_05.bmp12345678901234567890jn000_06.bmp12345678901234567890\x14\x010001
        """
        buf = StringIO.StringIO(jonbin)
        isContainsAttackBox(buf)

    def test_isContainsAttackBox_returnsFalse_whenThereAre2sprites(self):
        jonbin = """
        JONBx00\x02\x00jn000_05.bmp12345678901234567890jn000_06.bmp12345678901234567890\x14\x010000
        """
        buf = StringIO.StringIO(jonbin)
        isContainsAttackBox(buf)
