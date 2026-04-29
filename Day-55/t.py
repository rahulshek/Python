class Bank:
    def __init__(self, name, ph , pas):
        self.name = name
        self._ph = ph
        self.__pas = pas

    @property
    def get_password(self):
        return self.__pas
    
    @get_password.setter
    def get_password(self, new_password):
        self.__pas = new_password


b1 = Bank("Rahul", 1234567890, "Rahul@123")
print(b1.name)
print(b1._ph)
print(b1.get_password)

# print(b1.__pas)

b1.get_password = "Rahul@456"
print(b1.get_password)
