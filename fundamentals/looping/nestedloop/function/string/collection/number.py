arr1=[1,2,4,5,6,8,10]

arr1.sort()

i=0

j=1

for i in range(0,len(arr1)-1):
    j=i+1

    result=arr1[j] -arr1[i]

    if result!=1:
        print(arr1[i]+1,"is missing")
    




