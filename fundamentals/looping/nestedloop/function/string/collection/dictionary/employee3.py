employee={"id":1234,"name":"nandhu","department":"hr","age":27,"salary":35000}

#print(employee)

print(employee.get("department"))

print(employee.pop("age")) #pop: to remove 

print(employee)

#return all keys

for k in employee.keys():
    print(k)

#fetch all the values

for v in employee.values():
    print(v)

    #fetch key and values iteam()

    for k,v in employee.items():
        print(k,v)