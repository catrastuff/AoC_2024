with open("data_1.txt", "r") as f:
    order_data: list[str] = f.read().split("\n")

with open("data_2.txt", "r") as f:
    update_data: list[str] = f.read().split("\n")

def respect_rules(check_this: list[int], rule_list: list[list[int]]) -> bool:
    for rule in rule_list:
        try:
            if check_this.index(rule[0]) > check_this.index(rule[1]):
                return False
        except ValueError:
            pass
    else:
        return True

rules: list[list[int]] = [list(map(int, item.split("|"))) for item in order_data]
rules = sorted(rules, key=lambda x: x[0])
updates: list[list[int]] =  [list(map(int, item.split(","))) for item in update_data]

count = 0
for item in updates:
    if respect_rules(item, rules):
        continue
    fixed_list = [item.pop(0)]
    while item:
        next_value = item.pop(0)
        for i in range(len(fixed_list) + 1):
            fixed_list.insert(i, next_value)
            if not respect_rules(fixed_list, rules):
                fixed_list.pop(i)
            else:
                break
        else:
            assert False
    else:
        assert len(fixed_list) % 2 == 1
        count += fixed_list[len(fixed_list) // 2]
print(count)
