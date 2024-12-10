import dataclasses

with open("data.txt", "r") as f:
    data_input = f.read()


@dataclasses.dataclass
class DataBlock:
    space: int = 0
    is_free: bool = False
    id: int = 0

data: list[DataBlock] = []
id = 0
for i, char in enumerate(data_input):
    if i % 2 == 1:
        data.append(DataBlock(space=int(char), is_free=True, id=-1))
    else:
        data.append(DataBlock(space=int(char), is_free=False, id=id))
        id += 1

def move(data: list[DataBlock]) -> tuple[list[DataBlock], DataBlock | None]:
    if data[-1].is_free:
        return (data[:-1], None)
    elif not data[0].is_free:
        return (data[1:], data[0])
    ## Guarantee that starts with empty, ends with data
    free = data.pop(0)
    to_write = data.pop()
    if free.space > to_write.space:
        free.space = free.space - to_write.space
        data.insert(0, free)
        data.insert(0, to_write)
    elif free.space == to_write.space:
        data.insert(0, to_write)
    elif free.space < to_write.space:
        to_write_slice = DataBlock(space=(to_write.space - free.space), is_free=False, id=to_write.id)
        to_write.space = free.space
        data.insert(0, to_write)
        data.append(to_write_slice)
    return (data, None)

ordered_data: list[DataBlock] = []
while data:
    result = move(data)
    data = result[0]
    if result[1]:
        ordered_data.append(result[1])
print(ordered_data)

count: int = 0
pos: int = 0
for item in ordered_data:
    if not item.is_free:
        count += sum([item.id * (pos + i) for i in range(item.space)])
        pos += item.space
print(count)