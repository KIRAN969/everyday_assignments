class Department:
    def __init__(self,dept):
        self.dept=dept
    def addstudents(self,name,rollno,add,clg,mob):
        print(name,rollno,add,clg,mob,self.dept)

deptname=input("enter department:")
c=Department(deptname)
name1=input("enter name:")
rollno1=int(input("enter rollno:"))
add1=input("enter add:")
clg1=input("enter clg:")
mob1=int(input("enter mob:"))

deptname=input("enter department:")
e=Department(deptname)
name2=input("enter name:")
rollno2=int(input("enter rollno:"))
add2=input("enter add:")
clg2=input("enter clg:")
mob2=int(input("enter mob:"))

c.addstudents(name1,rollno1,add1,clg1,mob1)
e.addstudents(name2,rollno2,add2,clg2,mob2)
