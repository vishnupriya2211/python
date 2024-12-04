numbers = {"a": -5, 'b': 10, 'c': -3, 'd': 7}

# Dictionary comprehension to convert values to their absolute values
absolute_values = {key: abs(value) for key, value in numbers.items()}

# Print the resulting dictionary
print(absolute_values)
