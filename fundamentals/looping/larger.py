num1=int(input("enter the number1:"))

num2=int(input("enter the number2:"))

num3=int(input("enter the number3:"))

if num1>num2 and num1>num3:
    largest_num=num1
    second_largest=num2 if num2>num3 else num3
    
elif  num2>num1 and num2>num3:
      largest_num=num2
      second_largest=num1 if num1>num3 else num3
      
else:
    if num3>num1 and num3>num2:
     largest_num=num3
    second_largest=num1 if num1>num2 else num2
    
print("largest number is",largest_num)
print("second largest number is",second_largest)
