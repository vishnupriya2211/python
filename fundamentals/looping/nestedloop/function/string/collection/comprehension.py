arr=[2,3,4,5,6,7]

cubes=[]

for num in arr:
    cubes.append(num**3)
print(cubes)

#reference=[return loop condition]

squares=[num**2 for num in arr]

print(squares)