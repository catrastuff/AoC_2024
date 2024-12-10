with open("data.txt", "r") as f:
    input_data = f.read().split('\n')

safe_levels: int = 0
for line in input_data:
    levels: list[int] = [int(item) for item in line.split(' ')]
    increasing = True if levels[1] > levels[0] else False
    last_level = -1
    for level in levels:
        if last_level == -1:
            last_level = level
        else:
            dist = level - last_level
            if not (0 < abs(dist) < 4):
                break
            if (dist > 0 and increasing) or (dist < 0 and not increasing):
                last_level = level
            else:
                break
    else:
        safe_levels += 1
            

print(safe_levels)
