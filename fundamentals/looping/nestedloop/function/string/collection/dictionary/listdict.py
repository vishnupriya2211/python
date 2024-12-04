# Write a Python program to create a dictionary from a list of keys and values using dictionary comprehension.

keys = ["name", "age", "city"]

values = ["Anupama", 30, "kaloor"]

dictionary = {keys[i]: values[i] for i in range(len(keys))}

print(dictionary)
