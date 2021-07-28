class Employee:
    emp_name="Khan"

    def printName(self):
        print(self.emp_name)
Employee.printName=classmethod(Employee.printName)  
Employee.printName()
    