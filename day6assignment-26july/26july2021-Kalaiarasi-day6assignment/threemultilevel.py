class Person:
    def display(self,name):
        print(name)
class Employee(Person):
    def salaryy(self,salary):
        print(salary)
class Programmer(Employee):
    def program(self):
        print("programming")
per=Person()
emp=Employee()
pro=Programmer()
pro.salaryy("200000")
pro.display("sam")
emp.display("jai")