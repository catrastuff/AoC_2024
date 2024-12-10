with open("data.txt", "r") as f:
    rows: list[str] = f.read().split("\n")

rows_n = len(rows)
cols_n = len(rows[0])

dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]

guard_row_start: int = -1
guard_col_start: int = -1
guard_dir_start = 0
for i, r in enumerate(rows):
    if r.count("^"):
        j = r.find("^")
        guard_row_start = i
        guard_col_start = j
        rows[i] = f"{rows[i][:j]}.{rows[i][j+1:]}"
        break
else:
    print("Guard not found")

free_roam: set[tuple[int]] = {(guard_col_start, guard_row_start)}
guard_col = guard_col_start
guard_row = guard_row_start
guard_dir = guard_dir_start
while True:
    guard_col_next = guard_col + dirs[guard_dir][0]
    guard_row_next = guard_row + dirs[guard_dir][1]
    if not (-1 < guard_col_next < cols_n) or not (-1 < guard_row_next < rows_n):
        break
    if rows[guard_row_next][guard_col_next] == ".":
        guard_col = guard_col_next
        guard_row = guard_row_next
        if (guard_col, guard_row) not in free_roam:
            free_roam.add((guard_col, guard_row))
        else:
            continue
    else:
        guard_dir = (guard_dir + 1) % 4

obstacles: set[tuple] = set()
for obs_r in range(rows_n):
    for obs_c in range(cols_n):
        if rows[obs_r][obs_c] != ".":
            continue
        if (obs_c, obs_r) not in free_roam:
            continue
        rows[obs_r] = f"{rows[obs_r][:obs_c]}x{rows[obs_r][obs_c+1:]}"
        guard_col = guard_col_start
        guard_row = guard_row_start
        guard_dir = guard_dir_start
        visited: set[tuple[int]] = {(guard_col_start, guard_row_start, guard_dir_start)}
        while True:
            guard_col_next = guard_col + dirs[guard_dir][0]
            guard_row_next = guard_row + dirs[guard_dir][1]
            if not (-1 < guard_col_next < cols_n) or not (-1 < guard_row_next < rows_n):
                break
            if rows[guard_row_next][guard_col_next] == ".":
                guard_col = guard_col_next
                guard_row = guard_row_next
                if (guard_col, guard_row, guard_dir) not in visited:
                    visited.add((guard_col, guard_row, guard_dir))
                else:
                    obstacles.add((obs_r, obs_c))
                    break
            else:
                guard_dir = (guard_dir + 1) % 4
        rows[obs_r] = f"{rows[obs_r][:obs_c]}.{rows[obs_r][obs_c+1:]}"


print(len(obstacles))