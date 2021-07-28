num=5
print(str(num))
print(num.__add__(10)) #it is equvalent to + operator
print(int.__str__(num))# it is equvalent to str type casting
list1=[1,2,3]
print(list1.__len__())# it is equivalent to len function


class Magicmethods:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __repr__(self):
        return 'addition of two number' + ' '+str(int(self.a+self.b))
    def __str__(self):
        return str(self.a)+str(self.b)
    def __add__(self):
         return self.a+self.b
    
m=Magicmethods(1,2)
print(m)