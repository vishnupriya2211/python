from re import finditer

text=" i have 3 cars, 2 bikes and 1 cycle"

#pattern="\w" #alphanumeric
#pattern="\d" #chk digit 
#pattern="\D" #EXCLUDED digit
#pattern="\W"  #special character [^a-zA-Z0-9]
#pattern="\s" #space
pattern="\S" # exclude space

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())

