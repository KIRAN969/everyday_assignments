class Animal:
    def speak(self):
        print("Animal is speaking")

class Cat(Animal):
    def meows(self):
        print("Cat is meow")
d=Cat()
d.meows()
d.speak()        