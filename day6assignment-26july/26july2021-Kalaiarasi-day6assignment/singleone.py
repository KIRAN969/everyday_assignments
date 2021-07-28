class Animal:
    def eating(self,eat):
        self.eat=eat
        print(self.eat)
class dog(Animal):
    def barking(self,bark):
        self.bark=bark
        print(self.bark)
a=Animal()
d=dog()
a.eating("eating")
d.barking("barking")
d.eating("eating")
