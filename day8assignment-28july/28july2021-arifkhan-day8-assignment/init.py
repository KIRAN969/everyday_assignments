class Students:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Students(m1,m2)
        return s3


s1=Students(21,34)
s2=Students(24,56)
s3=s1+s2     #change to Student.__add__(s1,s2)
print(s3.m1)