def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
        print(fact)
result=factorial(3)

print(result)