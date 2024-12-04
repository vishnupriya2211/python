from re import fullmatch

user=input("enter the user input:")

pattern="([1-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,user)

if matcher==None:
    print("invalid")

else:

    print("valid")