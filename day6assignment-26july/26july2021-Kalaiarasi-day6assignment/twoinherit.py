class Person:
    def display(self,name,id,age):
        print(.name,id,age)
class student(Person):
    def grades(self,grade):
        print(grade)
p=Person()
s=student()
p.display("sam",1,20)
s.grades("A")
s.display("jai",2,20)
