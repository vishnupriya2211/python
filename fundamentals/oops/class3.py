class Person:
    name:str
    age:int
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display_person(self):
        print(self.name,self.age)

class Employee:
    emp_id:int
    salary:int

    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary

    def display_emplyee(self):
        print(self.emp_id,self.salary)

class Manager(Person,Employee):
    department:str



    def __init__(self, name, age, emp_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def display_manager(self):
        self.display_person()
        self.display_emplyee()
        print(self.department)

Employee_instance=Manager(32,"shifas","shiv1",55000,"hr")
Employee_instance.display_manager()