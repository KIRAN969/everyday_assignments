class Cars:
    color="brown"
    brand="BMW"

    def findMileage(self,li,km):
        return km/li

myCar=Cars()
a1=input("enter the color of car:")
a2=input("enter the brand of the car:")
l1=int(input("enter the litres:"))
l2=int(input("enter the kilometer:"))
Mileage=myCar.findMileage(l1,l2)
myCar.color=a1
myCar.brand=a2
print(myCar.color)
print(myCar.brand)
print(Mileage)

#printing default value of car
defaultCar=Cars()
print(defaultCar.color)
print(defaultCar.brand)