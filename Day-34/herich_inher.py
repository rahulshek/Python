
#& Create a class C , D , B which is inheriting the properties from common class A along with that create the properties for each class 

# class parent:
#     sname="Shekhawat"
#     address="Jaipur"
# class son(parent):
#     name="ABC"
#     age=20
# class daughter(parent):
#     name="DEf"
#     age=18

# print(daughter.sname)


#&Create a class develper and manager which is inheriting the properties from common class employee also create class member and object member for them respectively 

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name is {self.name} and salary is {self.salary}")
class developer(employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language
    def display(self):
        print(f"Name is {self.name} and salary is {self.salary} and language is {self.language}")
class manager(employee):
    def __init__(self,name,salary,team):
        super().__init__(name,salary)
        self.team=team
    def display(self):
        print(f"Name is {self.name} and salary is {self.salary} and team is {self.team}")
obj1=developer("Rahul",10000,"Python")
obj2=manager("Preksha",20000,"XYZ")
obj1.display()
obj2.display()
