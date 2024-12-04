from re import fullmatch

user=input("enter the user pan card number:")

pattern="[A-Z]{3}[PFCHAT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,user)

if matcher==None:

    print("invalid")

else:

    print("valid")