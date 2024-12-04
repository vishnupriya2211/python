from re import fullmatch

user=input("enter the user input:")

pattern="(KL)[0-9]{2}[A-Za-z]{1,2}[0-9]{1,4}"

matcher=fullmatch(pattern,user)

if matcher is None:

    print("invalid")

else:

    print("valid")