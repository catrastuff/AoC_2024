with open("data.txt", "r") as f:
    input_data: list[str] = f.read().split("\n")

def check(data: list[str]) -> bool:
    compose = ''.join(data)
    return ("MAS" in compose or "SAM" in compose)

rows = len(input_data)
cols = len(input_data[0])
count = 0

for i in range(rows):
    for j in range(cols):
        try:
            chars_NOSE = [input_data[i + k][j + k] for k in range(3)]
            chars_NESO = [input_data[i + k][j + 2 - k] for k in range(3) if j + 2 >= k]
        except IndexError:
            break
        else:
            compose_NOSE = ''.join(chars_NOSE)
            compose_NESO = ''.join(chars_NESO)
            count += 1 if check(chars_NOSE) and check(chars_NESO) else 0

print(count)