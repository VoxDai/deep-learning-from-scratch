from ch02.logic_gates import AND, NAND, OR, XOR


def test_and():
    assert AND(1, 1)
    assert not AND(1, 0)
    assert not AND(0, 1)
    assert not AND(0, 0)


def test_nand():
    assert not NAND(1, 1)
    assert NAND(1, 0)
    assert NAND(0, 1)
    assert NAND(0, 0)


def test_or():
    assert OR(1, 1)
    assert OR(1, 0)
    assert OR(0, 1)
    assert not OR(0, 0)


def test_xor():
    assert not XOR(1, 1)
    assert XOR(1, 0)
    assert XOR(0, 1)
    assert not XOR(0, 0)
