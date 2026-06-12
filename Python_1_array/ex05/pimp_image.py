import matplotlib.pyplot as plt
import numpy as np


def ft_invert(image: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    result = 255 - image
    plt.title("Inverted")
    plt.imshow(result)
    plt.show()
    return result


def ft_red(image: np.ndarray) -> np.ndarray:
    """Extracts the red channel of the image."""
    result = image * np.array([1, 0, 0], dtype=np.uint8)
    plt.title("Red")
    plt.imshow(result)
    plt.show()
    return result


def ft_green(image: np.ndarray) -> np.ndarray:
    """Extracts the green channel of the image."""
    result = image.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    plt.title("Green")
    plt.imshow(result)
    plt.show()
    return result


def ft_blue(image: np.ndarray) -> np.ndarray:
    """Extracts the blue channel of the image."""
    result = image.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    plt.title("Blue")
    plt.imshow(result)
    plt.show()
    return result


def ft_grey(image: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale."""
    grey = np.sum(image, axis=2) / 3
    result = image.copy()
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    plt.title("Grey")
    plt.imshow(result)
    plt.show()
    return result
