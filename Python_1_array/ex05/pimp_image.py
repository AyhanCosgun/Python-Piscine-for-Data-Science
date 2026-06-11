import matplotlib.pyplot as plt
import numpy as np


def ft_invert(image: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    result = 255 - image
    plt.imshow(result)
    plt.show()
    return result
