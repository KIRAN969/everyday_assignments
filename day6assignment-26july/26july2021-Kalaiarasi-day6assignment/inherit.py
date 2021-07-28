class Cars:
    def minecolor(self,color):
        self.color=color
        print(self.color)
class BMW(Cars):
    def topspeed(self,speed):
        self.speed=speed
        print(self.speed)
objc=Cars()
objBMW=BMW()
objc.minecolor("red")
#objc.topspeed(100)
objBMW.minecolor("blue")
objBMW.topspeed(50)