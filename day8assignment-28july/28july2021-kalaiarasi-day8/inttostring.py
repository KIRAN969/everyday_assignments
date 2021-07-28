#num=10
#print(str(num))
print(int.__str__(10))

class A:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return 'name: ' + self.name + '  salary: '+str(self.salary)
obj=A("kalai",10000)
print(obj)