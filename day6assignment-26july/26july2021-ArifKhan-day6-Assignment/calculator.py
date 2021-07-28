class Calculator:
    def addNum(self,a,b):
      return a+b

    def sub(self,a,b):
      return a-b

    def muli(self,a,b):
     return a*b 

    def div(self,a,b):
     return a/b

    def floorDiv(self,a,b):
        return a//b

Cal=Calculator()
num1=int(input("enter the first number:"))
num2=int(input("enter the second number"))
add=Cal.addNum(num1,num2)
sub=Cal.sub(num1,num2)
mulp=Cal.muli(num1,num2)
divp=Cal.div(num1,num2)
floor=Cal.floorDiv(num1,num2)
print(add)
print(sub)
print(mulp)
print(divp)
print(floor)


