number1=int(input("enter the number:"))

number2=int(input("enter the number:"))

try:
    number3=number1/number2

    print(number3)

except :
    number2=int(input("enter the number:"))
    number3=number1/number2

    print(number3)

finally:
    print("file write")

    print("database commit")

