# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the first 5 Fibonacci numbers
for _ in range(5):
    print(a)
    a, b = b, a + b
