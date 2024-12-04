from re import finditer

text="abababbababaab"

matcher=finditer("ab",text)

for m in matcher:

    print(m.group())
    print(m.start(),m.group())

    text=" i have 3 cars, 2 bikes and 1 cycle"
    tp=(10,)

    print(type(tp))