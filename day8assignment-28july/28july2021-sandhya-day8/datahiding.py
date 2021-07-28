class Employee:
    __name="sandhya"
obj=Employee()
#print(obj.__name) #it shows an error because __name we use __ for hide the data
print(obj._Employee__name)

