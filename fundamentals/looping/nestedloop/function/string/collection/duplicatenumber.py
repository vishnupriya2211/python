arr=[1,2,2,2,1,4,5]

arr.sort()

duplicate_number =[] # list il ilottu obj add cheyuna rethi result kazjin kaNNIKUM
for i in range(0,len(arr)-1):
    j=i+1

    result= arr[i] - arr[j]
    if result==0:

        if arr[i] not in duplicate_number:
            duplicate_number.append(arr[i])
        print(duplicate_number)