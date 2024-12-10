with open("data.txt", "r") as f:
    input_data: list[str] = f.read().split("\n")

def check(data: list[str]) -> bool:
    compose = ''.join(data)
    return ("XMAS" in compose or "SAMX" in compose)

rows = len(input_data)
cols = len(input_data[0])
count = 0

for i in range(rows):
    for j in range(cols):
        try:
            chars = [input_data[i][j + k] for k in range(4)]
        except IndexError:
            break
        else:
            count += 1 if check(chars) else 0

for i in range(rows):
    for j in range(cols):
        try:
            chars = [input_data[i + k][j] for k in range(4)]
        except IndexError:
            break
        else:
            count += 1 if check(chars) else 0

for i in range(rows):
    for j in range(cols):
        try:
            chars = [input_data[i + k][j + k] for k in range(4)]
        except IndexError:
            break
        else:
            count += 1 if check(chars) else 0

for i in range(rows):
    for j in range(cols):
        try:
            chars = [input_data[i + k][j - k] for k in range(4) if j >= k]
        except IndexError:
            break
        else:
            count += 1 if check(chars) else 0

print(count)