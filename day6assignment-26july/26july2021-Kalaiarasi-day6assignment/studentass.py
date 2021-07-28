class Students:
    def __init__(self,name,rollno,adminno):
        self.myname=name
        self.myroll=rollno
        self.myadmin=adminno
obj=[]
obj.append(Students("sam",11,3456))
obj.append(Students("jai",12,3457))
print(obj[0].myname)
print(obj[1].myname)
print(obj[1].myroll)