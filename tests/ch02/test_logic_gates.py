import unittest
from ch02.logic_gates import AND, NAND, OR, XOR


class TestLogicGates(unittest.TestCase):
    def test_and(self):
        self.assertTrue(AND(1, 1))
        self.assertFalse(AND(1, 0))
        self.assertFalse(AND(0, 1))
        self.assertFalse(AND(0, 0))

    def test_nand(self):
        self.assertFalse(NAND(1, 1))
        self.assertTrue(NAND(1, 0))
        self.assertTrue(NAND(0, 1))
        self.assertTrue(NAND(0, 0))

    def test_or(self):
        self.assertTrue(OR(1, 1))
        self.assertTrue(OR(1, 0))
        self.assertTrue(OR(0, 1))
        self.assertFalse(OR(0, 0))

    def test_xor(self):
        self.assertFalse(XOR(1, 1))
        self.assertTrue(XOR(1, 0))
        self.assertTrue(XOR(0, 1))
        self.assertFalse(XOR(0, 0))


if __name__ == '__main__':
    unittest.main()
