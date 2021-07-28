#class A(object):
  # def  __new__(cls)
  #      print("Creating instance")
  
    # It is not called
  #  def __init__(self):
  #      print("Init is called")
  
#print(A())

class A(object):
    
    def __new__(cls):
        print("Creating instance")
        return "khan"
  
class B(object):
    
    def __init__(self):
        print("Initializing instance")
        return "Arif "
  
print(A())
print(B())