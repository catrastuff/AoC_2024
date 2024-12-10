with open("data_1.txt", "r") as f:
    order_data: list[str] = f.read().split("\n")

with open("data_2.txt", "r") as f:
    update_data: list[str] = f.read().split("\n")

rules: list[list[int]] = [list(map(int, item.split("|"))) for item in order_data]
rules = sorted(rules, key=lambda x: x[0])

updates: list[list[int]] =  [list(map(int, item.split(","))) for item in update_data]

count = 0
for item in updates:
    for rule in rules:
        try:
            if item.index(rule[0]) > item.index(rule[1]):
                break
        except ValueError:
            pass
    else:
        assert len(item) % 2 == 1
        count += item[len(item) // 2]

print(count)