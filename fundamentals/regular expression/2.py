from re import finditer

text=" i have 3 cars, 2 bikes and 1 cycle"

#pattern="[a-zA-z]" chk for all apha
#pattern="[a-z]" ck all lower case
#pattern="[a-zA-Z0]" ck for all alphanumeric
pattern="[0-9]" #chk for all digit
pattern="[^ak]" #exclude ak
pattern="[^akA-Z0-9,]" #exclude
pattern="\w" #alphanumeric
match=finditer(pattern,text)

for m in match:

  print(m.start(),"==>",m.group())

