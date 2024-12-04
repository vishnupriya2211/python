class editor:

    name:str

    vendor:str

    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor

    def displya(self):
        print(self.name,self.vendor)

    def __str__(self):
        return self.name

editor_instance1=editor("pycharm","microsoft")

editor_instance1.displya()

print(editor_instance1)