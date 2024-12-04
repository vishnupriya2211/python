from re import fullmatch

user=input("enter the user aadhar card number:")

pattern="[0-9]{4}[0-9]{4}[0-9]{4}"

matcher=fullmatch(pattern,user)

if matcher==None:

    print("invalid")

else:

    print("valid")