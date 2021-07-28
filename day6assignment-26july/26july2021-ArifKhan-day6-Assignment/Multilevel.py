class India:
    def alotNumber(self,number):
        print(number)
class CarManufacturer(India):
    def makeACar(self,brand,color,price):
        print(brand,color,price)
class Seller(CarManufacturer):
    def CustomerOrder(self,name,mobno):
        print(name,mobno)

objSeller=Seller()
objSeller.CustomerOrder("Arif",9898989898) 
objSeller.makeACar("ferari","red",20000)
objSeller.alotNumber("UP203414")               

