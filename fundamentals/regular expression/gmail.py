from re import fullmatch

user=input("enter the usere-mail id:")

pattern="[a-zA-Z0-9._%+-]+@gmail\.com"

matcher=fullmatch(pattern,user)

if matcher==None:
    print("invalid")

else:

    print("valid")

