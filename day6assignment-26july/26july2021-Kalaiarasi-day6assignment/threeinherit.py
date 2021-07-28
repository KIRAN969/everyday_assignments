class Stationary:
    def display(self,price):
        print(price)
class eraser(Stationary):
    def uses(self,erase):
        print(erase)
s=Stationary()
e=eraser()
s.display("20")
e.uses("erasing")
e.display("10")
