import numpy as np
from numpy.typing import NDArray

from common.activation_function import sigmoid, identity


def init_network() -> tuple[dict[int, NDArray], dict[int, NDArray]]:
    weights = {
        1: np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]),
        2: np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]),
        3: np.array([[0.1, 0.3], [0.2, 0.4]]),
    }

    bias = {
        1: np.array([0.1, 0.2, 0.3]),
        2: np.array([0.1, 0.2]),
        3: np.array([0.1, 0.2]),
    }

    return weights, bias


def forward(network: tuple[dict[int, NDArray], dict[int, NDArray]], x: NDArray) -> NDArray:
    weights, bias = network
    layer_count = len(weights)
    active = x

    for i in range(layer_count - 1):
        w = weights[i + 1]
        b = bias[i + 1]
        active = sigmoid(active @ w + b)

    w = weights[layer_count]
    b = bias[layer_count]
    active = identity(active @ w + b)

    return active
