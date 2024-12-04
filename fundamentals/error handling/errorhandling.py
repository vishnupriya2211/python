number1=int(input("enter the number:"))

number2=int(input("enter the number:"))

from json import load as l

try:
    number3=number1/number2

    print(number3)

except Exception as e:
    print(e)

print("file write")

print("database commit")

