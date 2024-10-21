def calculate_structure_sum(data):
    global summ
    if isinstance(data, int):
        summ += data
        return summ
    elif isinstance(data , str):
        summ += len(data)
        return summ
    else:
        for i in data:
            if isinstance(i,dict):
                for key in i.keys():
                    calculate_structure_sum(key)
                for value in i.values():
                    calculate_structure_sum(value)
            else:
                calculate_structure_sum(i)

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
summ = 0
calculate_structure_sum(data_structure)
print(summ)

