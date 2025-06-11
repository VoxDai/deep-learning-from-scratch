import numpy as np
from numpy.typing import NDArray


def heaviside(x: NDArray) -> NDArray:
    return (x > 0).astype(np.int_)


def sigmoid(x: NDArray) -> NDArray:
    return 1 / (1 + np.exp(-x))


def relu(x: NDArray) -> NDArray:
    return np.maximum(x, 0)


def identify(x: NDArray) -> NDArray:
    return x


def softmax(x: NDArray) -> NDArray:
    x -= x.max()
    return np.exp(x) / np.exp(x).sum()
