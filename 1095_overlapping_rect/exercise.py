TEST_DATA = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3)  # width, height
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }
]


def are_overlapping():
    area_covered = set()
    for rect in TEST_DATA:
        top_left, dimensions = rect["top_left"], rect["dimensions"]
        bottom_right = (top_left[0] + dimensions[0], top_left[1] + dimensions[1])
        print(f"{bottom_right=}")
        for x in range(top_left[0], bottom_right[0] + 1):
            for y in range(top_left[1], bottom_right[1] + 1):
                coord = (x, y)
                print(f"{coord=}")
                if coord in area_covered:
                    return True
                area_covered.add((x, y))
    return False


if __name__ == '__main__':
    print(are_overlapping())
