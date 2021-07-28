class cal:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
c=cal()

while(True):
    print("select an option:")
    print("\n")
    print("1.addition")
    print("2.subtraction")
    print("3.exit")
    choice=int(input("enter ur choice:"))
    a=int(input("enter a"))
    b=int(input("enter b"))
    if choice==1:
        print("addition selected")
        #a=int(input("enter a:"))
        #b=int(input("enter b:"))
        print("sum",c.add(a,b))
        break

    if choice==2:
        print("subtraction selected")
        #a=int(input("enter a:"))
        #b=int(input("enter b:"))
        print("sub",c.sub(a,b))
        break
       
    if choice==3:
        break
    