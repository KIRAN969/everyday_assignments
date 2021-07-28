class India:
    def alotnumber(self,number):
        print(number)
class carmanufacture(India):
    def makecar(self,brand,color):
        print(brand,color)
class seller(carmanufacture):
    def customerorder(self,name,mobno):
        print(name,mobno)
objseller=seller()
objseller.customerorder("abi",23344)
objseller.makecar("white",24235)
objseller.alotnumber("123345")