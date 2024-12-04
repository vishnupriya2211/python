


class Person:
    name:str
    age:int

    def __init__(self,name,age) :
        self.name=name
        self.age=age
    @property
    def get_age(self):
        print(self.age)
    @property
    def get_name(self):
        print(self.name)

Person_instance=Person("hari",24)
Person_instance.get_name
        