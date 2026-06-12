import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Loads an image from the specified path
    and returns it as a NumPy array."""

    if not isinstance(path, str) or not path:
        print("Error: path must be a non-empty string.")
        return np.array([])

    try:
        with Image.open(path) as img:
            img = img.convert('RGB')
            array = np.array(img)
            return array
    except Exception as e:
        print(f"Error: could not load image from path '{path}'.\n{e}")
        return np.array([])
