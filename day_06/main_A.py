with open("data.txt", "r") as f:
    rows: list[str] = f.read().split("\n")

rows_n = len(rows)
cols_n = len(rows[0])

dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]

guard_row: int = -1
guard_col: int = -1
guard_dir = 0
for i, r in enumerate(rows):
    if r.count("^"):
        guard_row = i
        guard_col = r.find("^")
        break
else:
    print("Guard not found")

visited: set[tuple[int]] = {(guard_col, guard_row)}
while -1 < guard_col < cols_n and -1 < guard_row < rows_n:
    try:
        if rows[guard_row + dirs[guard_dir][1]][guard_col + dirs[guard_dir][0]] == ".":
            guard_col += dirs[guard_dir][0]
            guard_row += dirs[guard_dir][1]
            if (guard_col, guard_row) not in visited:
                visited.add((guard_col, guard_row))
        else:
            guard_dir = (guard_dir + 1) % 4
    except IndexError:
        break

print(len(visited))