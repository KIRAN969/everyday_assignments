from collections import namedtuple
Student = namedtuple('Student',['id','name','age'])
S = Student('1','kalai','21')
print(S[0])
print(S.name)
print(S.age)