num=int(input("enter a digit:"))

total=0

while(num!=0):
    digit=num %10
    total=total + digit
    print(total)
    num=num//10