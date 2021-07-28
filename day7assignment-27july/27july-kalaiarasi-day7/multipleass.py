class addoperation:
    def add(self,a,b):
        return a+b
class subtraction:
    def sub(self,a,b):
        return a-b
class multiplication:
    def mul(self,a,b):
        return a*b
class calculator(addoperation,subtraction,multiplication):
    pass
objcal=calculator()
n1=int(input("enter:"))
n2=int(input("enter:"))
print(objcal.add(n1,n2))
#print(objcal.sub(n1,n2))
#print(objcal.mul(n1,n2))
print(issubclass(calculator,subtraction))
print(issubclass(subtraction,addoperation))