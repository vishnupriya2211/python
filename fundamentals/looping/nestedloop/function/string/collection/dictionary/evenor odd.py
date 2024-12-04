arr=[10,20,30,40,2,3]

even_number={num:num**2 for num in arr if num % 2==0}

print("even number",even_number)

odd_number={num:num**3 for num in arr if num % 2!=0}

print("odd number",odd_number)