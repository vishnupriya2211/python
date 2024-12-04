fruits = ["apple", "banana", "cherry", "date"]

prices = [100, 70, 250, 300]


fruit_prices = {fruits[i]: prices[i] for i in range(len(fruits))}


print(fruit_prices)
