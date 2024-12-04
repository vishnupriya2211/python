array=[2,3,4,5]

#sum=0

#sum=array[3]+array[1]

#print(sum)

sum=8

for i in range(0,len(array)-1):

    for j in range(i+1,len(array)):

        current_sum=array[i] +array[j]

        if current_sum==sum:

            print(array[i] , array[j])

            break