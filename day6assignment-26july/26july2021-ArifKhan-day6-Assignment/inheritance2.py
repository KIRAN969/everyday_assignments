class mobile:
    def mycolor(self,color):
        self.color=color
        print(self.color)
class brand(mobile):
    def realme (self,ios):
        self.ios=ios
        print(self.ios)
obj1=mobile()
obj2=brand()
obj1.mycolor("Red")
obj2.realme("Apple iphone")