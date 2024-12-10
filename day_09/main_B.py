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
        return (data[:-1], data[-1])
    to_insert = data.pop()
    for i, item in enumerate(data):
        if item.is_free:
            if to_insert.space < item.space:
                empty_slice = DataBlock(space=(item.space - to_insert.space), is_free=True, id=-1)
                data[i] = to_insert
                data.insert(i+1, empty_slice)
                return (data, DataBlock(space=to_insert.space, is_free=True, id=-1))
            elif to_insert.space == item.space:
                data[i] = to_insert
                return (data, DataBlock(space=to_insert.space, is_free=True, id=-1))
    else:
        return (data, to_insert)

ordered_data: list[DataBlock] = []
while data:
    result = move(data)
    data = result[0]
    ordered_data.append(result[1])
ordered_data.reverse()

count: int = 0
pos: int = 0
for item in ordered_data:
    if not item.is_free:
        count += sum([item.id * (pos + i) for i in range(item.space)])
    pos += item.space
print(count)