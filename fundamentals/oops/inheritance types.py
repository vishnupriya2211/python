class GrandParent:
    def m(self):
        print("grand parents class m1 method")

class Parent():
        def m(self):
            print("print class m2 method")

class Child(Parent,GrandParent):
        def m3(self):
            print("child class m3 method")
child_instance=Child()

child_instance.m3()

child_instance.m()

