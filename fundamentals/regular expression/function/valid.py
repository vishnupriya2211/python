from re import fullmatch

user=input("enter the user input:")

patter="{}"


matcher=fullmatch(user,patter)

if matcher==None:

    print("invalid")

else:

    print("valid")

