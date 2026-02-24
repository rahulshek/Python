

#~----------Encapsulation-------~#


from abc import ABC,abstractmethod
class parent(ABC):
    
    @staticmethod
    def wakeup():
        print("I am from parent class")
    @abstractmethod
    def income():
        pass

class child(parent):
    @staticmethod
    def income():
        print("I earn only 20k")

# child.wakeup()
# c1=child()
child.income()

