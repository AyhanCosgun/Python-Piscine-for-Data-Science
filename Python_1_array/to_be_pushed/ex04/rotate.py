import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def manual_transpose(image: np.ndarray) -> np.ndarray:
    """Return the transposed version of the image given as a 2D Numpy array."""
    if not isinstance(image, np.ndarray) or image.ndim != 2:
        raise ValueError("image must be a 2D NumPy array.")
    height, width = image.shape
    transposed = np.zeros((width, height), dtype=image.dtype)
    for y in range(height):
        for x in range(width):
            transposed[x, y] = image[y, x]

    return transposed


def crop_image(image: np.ndarray) -> np.ndarray:
    """Return a 400 by 400 single-channel crop of the image."""
    if not isinstance(image, np.ndarray) or image.ndim != 3:
        raise ValueError("image must be a three-dimensional NumPy array.")

    if image.shape[0] < 500 or image.shape[1] < 850:
        raise ValueError("image is too small for the selected zoom area.")

    return image[100:500, 450:850, 0:1]


def main():
    """Load, crop, print, and display the transposed animal image."""
    try:
        image = ft_load("animal.jpeg")

        if image.size == 0:
            return

        cropped = crop_image(image)

        print(f"The shape of image is: {cropped.shape}")
        print(cropped)

        matrix_2d = cropped[:, :, 0]
        transposed = manual_transpose(matrix_2d)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        plt.imshow(transposed, cmap='gray')
        plt.tick_params(axis='both', labelsize=20)
        plt.show()

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
