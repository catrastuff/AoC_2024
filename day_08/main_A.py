import itertools

with open("data.txt", "r") as f:
    input_map = f.read().splitlines("\n")

antennas: dict[str, list[tuple[int]]] = {}

for i, row in enumerate(input_map):
    for j, char in enumerate(row):
        if char == ".":
            continue
        if char not in antennas.keys():
            antennas[char] = [(j, i)]
        else:
            antennas[char].append((j, i))

bound_X = len(row)
bound_Y = len(input_map)

def check_if_in_map(point: tuple[int]) -> bool:
    if not (-1 < point[0] < bound_X):
        return False
    elif not (-1 < point[1] < bound_X):
        return False
    else:
        return True

antinodes: set[tuple[int]] = set()

for freq in antennas.keys():
    for pair in itertools.combinations(antennas[freq], 2):
        delta = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
        resonance_A = (pair[0][0] + delta[0], pair[0][1] + delta[1])
        if check_if_in_map(resonance_A):
            antinodes.add(resonance_A)
        resonance_B = (pair[0][0] - 2 * delta[0], pair[0][1] - 2 * delta[1])
        if check_if_in_map(resonance_B):
            antinodes.add(resonance_B)

print(len(antinodes))
