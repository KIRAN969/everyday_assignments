class Person:
    def __init__(self,name):
        self.myname=name
    def saymyname(self):
        print(self.myname)
n=input("enter name:")
p=Person(n)
p.saymyname()