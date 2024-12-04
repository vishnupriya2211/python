from re import fullmatch

user = input("Enter the user input:")

pattern = "[P-Tp-t][369][A-Za-z0-9@]*"

matcher = fullmatch(pattern, user)

if matcher is None:
    print("invalid")
else:
    print("valid")





