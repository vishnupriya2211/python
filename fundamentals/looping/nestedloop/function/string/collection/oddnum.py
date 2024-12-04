arr=[2,3,4,5,6,7]

odd_num=[num for num in arr if num % 2!=0]

print(odd_num)

even_num=[num for num in arr if num % 2==0]

print(even_num)

numbwe_gt_five=[num for num in arr if num >5]

print(numbwe_gt_five)

map_num=[num+1 if num > 5 else num-1 for num in arr]

print(map_num)