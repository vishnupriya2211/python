from re import fullmatch

f=open("C:\\Users\\micvi\\OneDrive\\Desktop\\pythonworks\\fundamentals\\regular expression\\refile\\phone_number.txt")

for line in f:

    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher!=None:

        print(phone)

    else:

        print("invalid:",phone)

      