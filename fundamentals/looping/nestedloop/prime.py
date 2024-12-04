start=int(input("enter the number:"))

end=int(input("enter the ending number:"))

for num in range(start,end+1):
    
    is_prime=True

    for i in range(2, num):
        
        if num%i==0:
            
            is_prime=False

            break
    if is_prime==True:

        print(num)
