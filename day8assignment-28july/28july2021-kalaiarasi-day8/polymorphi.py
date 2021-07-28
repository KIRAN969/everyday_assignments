class A:
   def sayhello(self):
        print("hello")
class B:
    def sayhello(self):
       print("hai")
objA=A()
objB=B()
objA.sayhello()
objB.sayhello()

def add(a,b,c=0):  #methodoverloading
    return a+b+c
print(add(2,3))
print(add(2,3,4))