class Cars:
    def minecolour(self,colour):
        self.colour=colour
        print(self.color)

class BMW(Cars):
    def topSpeed(self,speed):
        self.speed=speed
        print(self.speed)

objCars=Cars()
objBMW=BMW()
#objCars.mineColour("Blue")
objBMW.topSpeed(150)


