with open("data.txt", "r") as f:
    input_data: list[str] = f.read().split('\n')

def can_be_from(value: int, numbs: list[int]) -> bool:
    if len(numbs) == 1:
        return value == numbs[0]
    test_numb = numbs[-1]
    if value % test_numb == 0:
        if can_be_from(value // test_numb, numbs[:-1]):
            return True
        elif can_be_from(value - test_numb, numbs[:-1]):
            return True
        else:
            return False
    else:
        return can_be_from(value - test_numb, numbs[:-1])

count: int = 0
for row in input_data:
    value: int = int(row.split(":")[0].strip())
    numbers: list[int] =  [int(n.strip()) for n in row.split(":")[1].split(" ") if n]
    if can_be_from(value, numbers):
        count += value

print(count)