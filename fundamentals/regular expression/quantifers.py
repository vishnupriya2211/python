from re import finditer

text="ababababababababaaaab"
#     012345678901234567890
#pattern="a{2}"
#pattern="a{1,3}" #1: mini one , max 3
#pattern="a*" #any number including 0
#pattern="[a-z]{3}" 
#pattern="[a-z]{1,3}"
pattern="[a-z]{2}[0-9]{2}"
pattern="\s" #space

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),m.group())