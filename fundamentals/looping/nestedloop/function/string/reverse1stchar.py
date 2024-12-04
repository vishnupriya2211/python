text="hellopython"

at_index=text.index("p")

name=text[at_index-1::-1]

balance_str=text[at_index:]

result=name+balance_str

print(result)