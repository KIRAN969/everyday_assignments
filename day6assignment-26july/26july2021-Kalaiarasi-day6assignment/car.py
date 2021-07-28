class Cars:
    color="black"
    brand="BMW"

    def findmileage(self,li,km):
        return km/li
myCar=Cars()
a1=input("enter color:")
a2=input("enter brand:")
l=int(input("enter litre:"))
k=int(input("enter kilometer:"))

mileage=myCar.findmileage(l,k)
myCar.color=a1
myCar.brand=a2
print(myCar.color)
print(myCar.brand)

defaultcar=Cars()
print(defaultcar.color)
print(defaultcar.brand)
print(mileage)