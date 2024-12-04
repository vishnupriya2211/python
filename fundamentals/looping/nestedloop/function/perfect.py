def perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return True  
    else:
        return False  
# Example usage
print(perfect_number(5)) 
print(perfect_number(6))  
