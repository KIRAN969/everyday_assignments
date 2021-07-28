class A:
    def __init__(self,name): 
        self.name=name
    
    def __len__(self):
        return len(self.name)

obj=A("kalai")
print(len(obj))