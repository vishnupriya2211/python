from re import fullmatch

user=input("enter the user input:")

pattern="((18|19)[0-9]{2}|20[01][0-9]|202[0-4])"

matcher=fullmatch(pattern,user)

if matcher==None:
    print("invalid")

else:

    print("valid")