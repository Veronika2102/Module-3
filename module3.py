data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
count = 0
def dat(data):
    global count
    if isinstance(data, int):
        count += data
    elif isinstance(data, str):
        count += len(data)
    elif isinstance(data, dict):
        for key, value in data.items():
            dat(key)
            dat(value)
    elif isinstance(data, (list, tuple, set)):
        for i in data:
            dat(i)

for i in data_structure:
    dat(i)

print(count)












