class Faculity:
    name:str
    age:int
    course:str
    experience:int
    salary:int

    def set_Faculity(self,id,name,age,course,experience,salary):
     self.id=id
     self.name=name
     self.age=age
     self.course=course
     self.experience=experience
     self.salary=salary

    def display_Faculity(self):

        print(self.name,self.age,self.course)

faculity_instace1=Faculity()

faculity_instace2=Faculity()

faculity_instace2.set_Faculity(100,"vishnu",27,"python",5,50000)

faculity_instace2.display_Faculity()