import numpy as np


def AND(x1: float, x2: float) -> bool:
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -1.5
    val = x @ w + b
    return True if val > 0 else False


def NAND(x1: float, x2: float) -> bool:
    x = np.array([x1, x2])
    w = np.array([-1, -1])
    b = 1.5
    val = x @ w + b
    return True if val > 0 else False


def OR(x1: float, x2: float) -> bool:
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -0.5
    val = x @ w + b
    return True if val > 0 else False


def XOR(x1: float, x2: float) -> bool:
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)
