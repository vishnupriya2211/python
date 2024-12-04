start=int(input("enter the starting number:"))

end=int(input("enter the ending number:"))

reverse=True if start>end else False

i=start

while(i<=end if reverse==False else i>=end ):
    if i % 2 ==0:
        print(i)
    if reverse==False:
        i=i+1
    else:
        i=i-1


