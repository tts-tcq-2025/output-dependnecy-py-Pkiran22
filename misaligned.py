def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    mapping = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            mapping.append((i * 5 + j, major, minor))
    return mapping


def print_color_map():
    mapping = get_color_map()
    for entry in mapping:
        print(f'{entry[0]} | {entry[1]} | {entry[2]}')
    return len(mapping)

color_map = get_color_map()
assert color_map[0] == (0, 'White', 'Blue')
assert color_map[24] == (24, 'Violet', 'Slate')
assert len(color_map) == 25  # still OK

print("All is well (maybe!)")
