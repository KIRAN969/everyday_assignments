class Calculator():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def floor(self,a,b):
        return a//b
    def mod(self,a,b):
        return a%b
    def exp(self,a,b):
        return a**b
a=int(input("enter a:"))
b=int(input("enter b:"))
obj1=Calculator()
print(obj1.add(a,b))
print(obj1.sub(a,b))
print(obj1.mul(a,b))
print(obj1.div(a,b))
print(obj1.floor(a,b))
print(obj1.mod(a,b))
print(obj1.exp(a,b))