#arr=[10,8,7,12,13,20,25]

#arr.sort()

#serch_element=int(input("enter the number:"))

#is_present=False

#low=0

#upper=len(arr)-1

#while(low<=upper):

   # mid=(low + upper)//2

   # if serch_element == arr[mid]:
   #     is_present=True
   #     break

   #elif serch_element< arr[mid]:
  #      upper=mid-1

    #elif serch_element> arr[mid]:
      #  low=mid+1
    
    #print(is_present)


arr = [10, 8, 7, 12, 13, 20, 25]

# Sorting the array
arr.sort()

# Input the number to search
serch_element = int(input("Enter the number: "))

is_present = False

low = 0
upper = len(arr) - 1

# Binary search algorithm
while low <= upper:
    mid = (low + upper) // 2
    
    if serch_element == arr[mid]:
        is_present = True
        break
    elif serch_element < arr[mid]:
        upper = mid - 1
    else:
        low = mid + 1

# Print the result after search is completed
print(is_present)
