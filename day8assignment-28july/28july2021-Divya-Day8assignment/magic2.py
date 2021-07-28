class Employee:
    raise_amt = 500

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp1 = Employee('divya','k',50000)
emp2 = Employee('Ayvid','ay',10000)

print(emp1 + emp2)
print(len(emp1))
print(str(emp1))
print(repr(emp2))
