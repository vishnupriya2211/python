num_start=int(input("enter the starting number:"))

num_end=int(input("enter the ending number:"))

if num_start>num_end:
    num_start,num_end=num_end,num_start
    
num=num_start

while(num<=num_end):

    if num % 2 !=0:

        print(num)
    
    num=num+1