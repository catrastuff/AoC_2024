with open("data.txt", "r") as f:
    input_data = f.read().split('\n')

input_l: list[int] = []
input_r: list[int] = []

for line in input_data:
    le, ri = line.split("   ", maxsplit=1)
    input_l.append(int(le))
    input_r.append(int(ri))

assert len(input_l) == len(input_r)

total: int = 0
while len(input_l) > 0:
    min_l = min(input_l)
    min_r = min(input_r)
    dist = abs(min_l - min_r)
    total += dist
    input_l.remove(min_l)
    input_r.remove(min_r)

print(total)