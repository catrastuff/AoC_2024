with open("data.txt") as f:
    input_data = f.read()

start: list[str] = [int(i) for i in input_data.split(" ")]
stone_values: dict[int, int] = {}
for item in start:
    if item in stone_values:
        stone_values[item] += 1
    else:
        stone_values[item] = 1

def blink_stone(value: int) -> list[int]:
    if value == 0:
        return [1]
    elif len(str(value)) % 2 == 0:
        return [int(str(value)[:len(str(value)) // 2]), int(str(value)[len(str(value)) // 2:])]
    else:
        return [value*2024]

for i in range(75):
    next_gen: dict[int, int] = {}
    for stone in stone_values:
        stones = blink_stone(stone)
        for to_add in stones:
            times = stone_values[stone]
            if to_add in next_gen:
                next_gen[to_add] += times
            else:
                next_gen[to_add] = times
    stone_values = next_gen

count : int = 0
for key in stone_values:
    count += stone_values[key]
print(count)