# create a function last digit max with two parameters num1 , num2



def max(num1, num2):
    num1_max=num1%10

    num2_max=num2%10

    print( num1 if num1_max> num2_max else num2)
print(max(123,874))