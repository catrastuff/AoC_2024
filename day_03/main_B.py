import re

with open("data.txt", "r") as f:
    input_data = f.read()

input_data = re.sub(r"don't\(\).*?do\(\)", "", input_data, flags=re.DOTALL)
total = sum([int(item.group(1)) * int(item.group(2)) for item in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", input_data, flags=re.DOTALL)])

print(total)