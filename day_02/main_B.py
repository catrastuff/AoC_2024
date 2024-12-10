with open("data.txt", "r") as f:
    input_data = f.read().split('\n')

def is_safe(input: list[int]) -> bool:
    increasing = True if input[1] > input[0] else False
    last_level = -1
    errors = 0
    for level in input:
        if last_level == -1:
            last_level = level
        else:
            dist = level - last_level
            if not (0 < abs(dist) < 4):
                errors +=1
                if errors > 1:
                    return False
            elif (dist > 0 and increasing) or (dist < 0 and not increasing):
                last_level = level
            else:
                errors +=1
                if errors > 1:
                    return False
    else:
        if errors:
            print(input, errors)
        return True

safe_levels: list[list[int]] = []
for line in input_data:
    levels: list[int] = [int(item) for item in line.split(' ')]
    if is_safe(levels):
        safe_levels.append(levels)
    else:
        levels.reverse()
        if is_safe(levels):
            safe_levels.append(levels)

print(len(safe_levels))
