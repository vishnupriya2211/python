arr = [2, 3, 4, 5, 6, 7, 8, 9]

left = 0
right = len(arr) - 1
sum = 7

while left < right:
    current_sum = arr[left] + arr[right]
    
    if current_sum == sum:
        print(arr[left], arr[right])  # Print the pair, not their sum
        break
    elif current_sum > sum:
        right = right - 1  # Move right pointer left
    else:
        left = left + 1  # Move left pointer right

