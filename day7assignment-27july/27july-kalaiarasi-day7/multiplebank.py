class RBI:
    def rateofinterest(self):
        print(8)
class SBI(RBI):
    def rateofinterest(self):
        print(7)
class AXIS(RBI):
    def rateofinterest(self):
        print(6)
s=SBI()
a=AXIS()
s.rateofinterest()
a.rateofinterest()
r=RBI()
r.rateofinterest()