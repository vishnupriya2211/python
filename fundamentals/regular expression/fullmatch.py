from re import fullmatch

user=input("enter the user input:")

pattern="[A-Za-z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user)

if matcher==None:
    print("invalid")

else:

    print("valid")