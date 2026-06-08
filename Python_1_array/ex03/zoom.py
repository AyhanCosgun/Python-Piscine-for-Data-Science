import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def zoom_image(image: np.ndarray) -> np.ndarray:
    """Return a 400 by 400 single-channel crop of the image."""
    if not isinstance(image, np.ndarray) or image.ndim != 3:
        raise ValueError("image must be a three-dimensional NumPy array.")

    if image.shape[0] < 500 or image.shape[1] < 850:
        raise ValueError("image is too small for the selected zoom area.")

    return image[100:500, 450:850, 0]


def main():
    """Load, crop, print, and display the animal image."""
    try:
        image = ft_load("animal.jpeg")

        if image.size == 0:
            return

        print(image)

        zoomed = zoom_image(image)

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        plt.imshow(zoomed, cmap="gray")
        plt.show()

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
