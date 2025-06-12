import numpy as np
import pytest

from ch03.three_layer_network import init_network, forward


def test_forward():
    x = np.array([1.0, 0.5])
    y = forward(init_network(), x)

    assert y == pytest.approx(np.array([0.31682708, 0.69627909]))
