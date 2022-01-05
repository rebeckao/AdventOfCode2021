from typing import List


def lit_pixels_after_passes(image_enhancement_algorithm: str, image: List[str], passes: int):
    margin = 10
    for step in range(0, passes):
        width = len(image[0])
        empty_line = "".ljust(width + margin * 2, ".")
        enlarged_image = [empty_line for _ in range(0, margin)]
        side_margin = "".ljust(margin, ".")
        enlarged_image.extend([side_margin + original + side_margin for original in image])
        enlarged_image.extend([empty_line for _ in range(0, 5)])
        new_image = [empty_line for _ in enlarged_image]
        for row_idx in range(1, len(enlarged_image) - 1):
            for col_idx in range(1, len(enlarged_image[0]) - 1):
                number = enlarged_image[row_idx - 1][col_idx - 1: col_idx + 2] \
                         + enlarged_image[row_idx][col_idx - 1: col_idx + 2] \
                         + enlarged_image[row_idx + 1][col_idx - 1: col_idx + 2]
                decimal = _binary_to_decimal(number.replace("#", "1").replace(".", "0"))
                new_pixel = image_enhancement_algorithm[decimal]
                new_image[row_idx] = new_image[row_idx][0: col_idx] + str(new_pixel) + new_image[row_idx][col_idx + 1:]
        image = new_image
        if step % 2 == 1:
            pruned_image = [line[margin * 2 - 2:-(margin * 2 - 2)] for line in image[margin * 2 - 2:-margin + 2]]
            image = pruned_image
    for line in image:
        print(line)
    return sum([line.count("#") for line in image])


def _binary_to_decimal(binary: str) -> int:
    return sum([int(value) * pow(2, (len(binary) - idx - 1)) for idx, value in enumerate(binary)])
