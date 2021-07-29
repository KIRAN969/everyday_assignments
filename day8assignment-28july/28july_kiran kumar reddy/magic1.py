class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst=object.__new__(cls)
        return inst
    def __init(self):
        print("__init__magic method is called")
        self.name='kiran'
        print(self.name)
ob=Employee()