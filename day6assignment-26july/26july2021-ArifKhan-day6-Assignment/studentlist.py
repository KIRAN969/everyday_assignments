#list of object
class Students:
    def __init__(self,name,rollno,admin):
        self.myname=name
        self.myrollno=rollno
        self.myadmin=admin 
obj=[]
obj.append(Students("ram",12,234)) 
obj.append(Students("khan",13,231)) 
obj.append(Students("Gulshan",14,236))
print(obj[0].myname)
print(obj[0].myrollno)