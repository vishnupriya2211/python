number=int(input("enter a digit:"))

total=0

while number !=0:
    digit=number %10
    num_sqrt=digit**2
    total=total+num_sqrt
    
    number=number//10
print(total)
