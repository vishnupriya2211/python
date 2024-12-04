class Student:
    id: int
    name: str
    course: int
    
    def set_student(self, id, name, course):
        self.id = id
        self.name = name
        self.course = course
        

    def display_student(self):
        print(self.id, self.name, self.course)

# Create an instance of Employee
emp_instance = Student()

# Set employee details
emp_instance.set_student(100, "Vishnu priya","Computer science")

# Display employee details
emp_instance.display_student()
