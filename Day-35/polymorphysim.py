

#~----------------------------------Polymorphism-----------------------------~#

#~------------------Method Overriding-----------------------------~#

# class A:
#     def display(self):
#         print("Display of class A")

# class B(A):
#     def display(self):
#         print("Display of class B")

# obj1=A()
# obj2=B()
# obj1.display()
# obj2.display()

#~------------------Operator Overloading-----------------------------~#

class sample:
    def __init__(self,value1,value2):
        self.VALUE1=value1
        self.VALUE2=value2
        
    def __add__(self, other):
        return self.VALUE1+other.VALUE2
    
    def __sub__(self, other):
        return self.VALUE1-other.VALUE2
    
    def __mul__(self, other):
        return self.VALUE1*other.VALUE2
    
    def __str__(self):
        return f"{self.VALUE1} and {self.VALUE2}"
    
    def __truediv__(self, other):
        return self.VALUE1/other.VALUE2

ob1=sample(10,20)
ob2=sample(30,40)
print(ob1+ob2)
print(ob1-ob2)
print(ob1*ob2)
print(ob1)
print(ob2)
print(ob1.__repr__())