with open("data.txt") as f:
    input_data = f.read()

start: list[str] = [int(i) for i in input_data.split(" ")]

def blink_stone(value: int) -> list[int]:
    if value == 0:
        return [1]
    elif len(str(value)) % 2 == 0:
        return [int(str(value)[:len(str(value)) // 2]), int(str(value)[len(str(value)) // 2:])]
    else:
        return [value*2024]

stone_values = start
for i in range(25):
    next_gen: list[int] = []
    while stone_values:
        stone = stone_values.pop()
        next_gen.extend(blink_stone(stone))
    stone_values = next_gen

print(len(stone_values))