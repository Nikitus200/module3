def _dict(i):
    global s
    for keys, values in i.items():
        if isinstance(values, dict) == True:
            _dict(values)
        if isinstance(keys, tuple) == True:
            _tuple_list_set(keys)
        if isinstance(values, set) == True or isinstance(values, tuple) == True or isinstance(values, list) == True:
            _tuple_list_set(values)
        if isinstance(keys, int) == True:
            s += keys
        if isinstance(keys, str) == True:
            s += len(keys)
        if isinstance(values, int) == True:
            s += values
        if isinstance(values, str) == True:
            s += len(values)
def _tuple_list_set(i):
    global s
    for j in i:
        if isinstance(j, int) == True:
            s += j
        if isinstance(j, str) == True:
            s += len(j)
        if isinstance(j, dict) == True:
            _dict(j)
        if isinstance(j, set) == True or isinstance(j, tuple) == True or isinstance(j, list) == True:
            _tuple_list_set(j)

s = 0
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    global s
    for i in data_structure:
        if isinstance(i, dict) == True:
            _dict(i)
        if isinstance(i, set) == True or isinstance(i, tuple) == True or isinstance(i, list) == True:
            _tuple_list_set(i)
        if isinstance(i, int) == True:
            s += i
        if isinstance(i, str) == True:
            s += len(i)
    return s




result = calculate_structure_sum(data_structure)
print(result)