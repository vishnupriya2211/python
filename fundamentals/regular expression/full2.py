from re import fullmatch


user=input("enter the user input:")

pattern="(91)+[0-9]{10}"

matcher=fullmatch(pattern,user)

if matcher==None:
    print("invalid")

else:

    print("valid")