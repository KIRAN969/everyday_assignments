class a:
    def sayHello(self):
        print("Heelo")
class b(a):
    def sayHello(self):
        print("hi")
obja=a()
objb=b()
obja.sayHello()
objb.sayHello()

def add(a,b,c=0):
    return a+b+c
print(add(2,3))
print(add(2,3,4))
