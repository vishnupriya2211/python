class Mobile:
    name:str
    price:int
    brand:str

    def __init__(self,name,price,brand):
        self.name=name
        self.price=price
        self.brand=brand

    def display_mobile(self):

        print(self.name,self.price,self.brand)

Mobile_instance1=Mobile("oppo reno 12 pro",53000,"oppo")

Mobile_instance1.display_mobile()