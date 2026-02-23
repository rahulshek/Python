
#~-----------Encapsulation------------------#

#?It is a phenomenon of providing security to the data members by restricting their access outside the class.
#?It is achieved by using private access specifier.
#?Private access specifier is denoted by double underscore before the variable name.
#?Private variables can be accessed only within the class in which they are declared.
#?Private variables are not accessible outside the class.
#?Private variables are not accessible even by the child class.
#?Private variables are not accessible even by the friend class.
#?Private variables are not accessible even by the friend function.

#!Syntax:

#&Public

#! class Cname:
#! 	var=value
	
#! 	def mname(self,args):
#! 		<--S.B-->
	
#! 	@classmethod 
#! 	def mname(cls,args):
#! 		<--S.B-->
#! 	@staticmethod
#! 	def mname(args):
#! 		<--S.B-->

#*----------------------------------------------------------------------------------------------------------------------#

#&Protected

#! class Cname:
#! 	_var=value
	
#!	def _mname(self,args):
#! 		<--S.B-->
	
#! 	@classmethod 
#! 	def _mname(cls,args):
#! 		<--S.B-->
#! 	@staticmethod
#! 	def _mname(args):
#! 		<--S.B-->

#*----------------------------------------------------------------------------------------------------------------------#

#&Private

#! class Cname:
#! 	__var=value
	
#! 	def __mname(self,args):
#! 		<--S.B-->
	
#! 	@classmethod 
#! 	def __mname(cls,args):
#! 		<--S.B-->
#! 	@staticmethod
#! 	def __mname(args):
#! 		<--S.B-->

#*----------------------------------------------------------------------------------------------------------------------#

# class bank:
#     BNAME="SBI"
#     BRANCH="KOLKATA"
#     __BMANAGER="MR.X"
#     def __init__(self,accno,name,balance):
#         self.accno=accno
#         self.name=name
#         self.__balance=balance

# acc1=bank(123456789,"MR.A",10000)
# print(acc1.accno)
# print(acc1.name)
#! As a responsible devloper don't access private variables
# print(acc1._bank__BMANAGER) 
# print(acc1._bank__balance)  

#*----------------------------------------------------------------------------------------------------------------------#

#? To Access private object member 
# objname._classname__objectmembername

#? To modify private object member
# objname._classname__objectmembername=new_value

#? To Access private class member
# classname._classname__classmembername

#? To Modify Private class member
# classname._classname__classmembername=new_value

#*----------------------------------------------------------------------------------------------------------------------#

# class bank:
#     BNAME="SBI"
#     BRANCH="KOLKATA"
#     __BMANAGER="MR.X"
#     def __init__(self,accno,name,balance):
#         self.accno=accno
#         self.name=name
#         self.__balance=balance
    
#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self,value):
#         self.__balance=value

# acc1=bank(123456789,"MR.A",10000)
# print(acc1.get_balance())
# acc1.set_balance(20000)
# print(acc1.get_balance())

#*----------------------------------------------------------------------------------------------------------------------#