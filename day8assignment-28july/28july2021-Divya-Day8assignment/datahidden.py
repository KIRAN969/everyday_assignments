class A:
    __name = "DIvya" # hidden data underscore is an syntax

    def Test(self):
        print(__name)
objA = A()
# print(objA.__name()) #error
# print(objA.Test())   #error
print(objA._A__name)