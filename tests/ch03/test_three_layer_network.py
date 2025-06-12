import unittest

import numpy as np

from ch03.three_layer_network import init_network, forward


class TestThereLayerNetwork(unittest.TestCase):
    def test_forward(self):
        x = np.array([1.0, 0.5])
        y = forward(init_network(), x)
        self.assertAlmostEqual(float(y[0]), 0.31682708)
        self.assertAlmostEqual(float(y[1]), 0.69627909)


if __name__ == '__main__':
    unittest.main()
