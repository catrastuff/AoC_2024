with open("data.txt", "r") as f:
    input_data = f.read().split("\n")

rows = len(input_data)
cols = len(input_data[0])

starting_pos: list[tuple[int]] = [(i, int(j)) for i, line in enumerate(input_data) for j, char in enumerate(line) if char == '0']
ending_pos: list[tuple[int]] = [(i, int(j)) for i, line in enumerate(input_data) for j, char in enumerate(line) if char == '9']


def radiate(pos: tuple[int]) -> list[tuple[int]]:
    height = int(input_data[pos[0]][pos[1]])
    steps: list[tuple[int]] = []
    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        look_y = pos[0] + dir[0]
        look_x = pos[1] + dir[1]
        if not (-1 < look_y < rows) or  not (-1 < look_x < cols):
            continue
        if int(input_data[look_y][look_x]) == height + 1:
            steps.append((look_y, look_x))
    return steps

def is_reachable(start: tuple[int], end: tuple[int]) -> bool:
    if abs(start[0]-end[0]) + abs(start[1]-end[1]) > 10:
        return False
    paths: list[list[tuple[int]]] = [[start]]
    while paths:
        curr_path = paths.pop()
        steps = radiate(curr_path[-1])
        if end in steps:
            return True
        for step in steps:
            paths.append(curr_path + [step])
    else:
        return False

count: int = 0
for s in starting_pos:
    for e in ending_pos:
        if is_reachable(s, e):
            count += 1
print(count)