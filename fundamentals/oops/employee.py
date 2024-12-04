class Employee:
    id: int
    name: str
    age: int
    salary: int
    department: str

    def set_employee(self, id, name, age, department, salary):
        self.id = id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display_emp(self):
        print(self.id, self.name, self.age)

# Create an instance of Employee
emp_instance = Employee()

# Set employee details
emp_instance.set_employee(100, "Vishnu", 21, "HR", 35000)

# Display employee details
emp_instance.display_emp()
