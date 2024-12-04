list=[10,20,30,40,50]
 
list.sort()

for i in range(0,len(list)):

    for j in range(i,len(list)):

        sum=list[i] + list[j]

        print(sum)

        

