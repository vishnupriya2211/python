from re import fullmatch

user=input("enter the user input:")

pattern="(0?[1-9]|[12][0-9]|3[01])"

matcher=fullmatch(pattern,user)

if matcher==None:
    print("invalid")

else:

    print("valid")