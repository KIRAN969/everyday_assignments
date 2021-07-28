class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
class Babydog(Dog):
    def weep(self):
        print("weeping")
ani=Animal()
do=Dog()
baby=Babydog()
baby.weep()
baby.bark()
baby.eat()
do.eat()
