lst = [
    1, 2,
    [10, 20],
    [1, 2, 5, [10, 3]],
    100
]

list_obj = [item for item in lst if isinstance(item, list)]

print(list_obj)

print(max(list_obj, key=len))
