import sys, os

import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

sys.path.append(os.pardir)


def image_show(image):
    pil_img = Image.fromarray(np.uint8(image))
    pil_img.show()


if __name__ == '__main__':
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

    img = x_train[0]
    label = t_train[0]
    print(label)

    print(img.shape)
    img = img.reshape(28, 28)
    print(img.shape)

    image_show(img)
