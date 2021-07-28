class Department:
    def __init__(self,dept):
        self.dept=dept
    def addStudents(self):
        self.name=input("enter your name:")
        self.roll=int(input("enter the roll:"))
        self.admin=int(input("enter the admission"))
        self.college=input("enter you college:")
        self.add=input("enter the address")
        self.mob=int(input("enter the mobilenumber:"))
        print("department:",self.dept)
        print("students name:",self.name)
        print("student roll no:",self.roll)
        print("student addmin:",self.admin)
        print("student college:",self.college)
        print("student add:",self.add)
        print("student mobile number:",self.mob)
li11=Department("CSE")
li11.addStudents()
print("\n")
li2=Department("Electrical")
li2.addStudents()      
        



