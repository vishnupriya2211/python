start=int(input("enter the starting number:"))

end=int(input("enter the ending number:"))

if start<end:

    for num in range(start,end+1,1):

        print(num)
else:
    for num in range(start,end-1,-1):

        print(num)