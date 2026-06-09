import numpy as np

from load_image import ft_load


def main():
    image = ft_load(str("animal.jpeg"))

    if image.ndim == 3:
        image = image[:, :, 0]

    pattern = np.array([167, 180, 194])
    
    pattern_length = 3 #pattern.shape[0]

    matches: list[tuple[int, int]] = []
    last_col = image.shape[1] - pattern_length + 1

    for row_index in range(image.shape[0]):
        row = image[row_index]
        for col_index in range(last_col):
            if np.array_equal(row[col_index:col_index + pattern_length], pattern):
                matches.append((row_index, col_index))
                if len(matches) >= 50:
                    break

    for row_index, col_index in matches:
        print(f"({row_index}, {col_index})")


if __name__ == "__main__":
    main()