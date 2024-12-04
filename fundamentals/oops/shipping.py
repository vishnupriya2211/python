class Shipping:
    def calculate_shipping_coat(self,weight):
        print(weight*5)
class ExpressShipping(Shipping):
    def calculate_shipping_coat(self, weight):
        print(weight*20)
class StandardShipping(Shipping):
    def calculate_shipping_coat(self, weight):
        print(weight*10)
expe_instance=ExpressShipping()

expe_instance.calculate_shipping_coat(10)

strd_instance=StandardShipping()

strd_instance.calculate_shipping_coat(10)