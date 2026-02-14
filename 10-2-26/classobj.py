
# class Qspider:
#     Branch="Ahmedabad"
#     no_of_class=6
#     timing="10 to 8"

# s1=Qspider()
# s2=Qspider()


#Modifying class members using object reference
# print(Qspider.Branch,Qspider.no_of_class,Qspider.timing)
# print(s1.Branch,s1.no_of_class,s1.timing)
# print(s2.Branch,s2.no_of_class,s2.timing)
# s1.timing="9 to 6"
# print("After")
# print(Qspider.Branch,Qspider.no_of_class,Qspider.timing)
# print(s1.Branch,s1.no_of_class,s1.timing)
# print(s2.Branch,s2.no_of_class,s2.timing)

#Modifying class members using class name
# print(Qspider.Branch,Qspider.no_of_class,Qspider.timing)

# Qspider.timing="9 to 6"
# print(Qspider.Branch,Qspider.no_of_class,Qspider.timing)
# print(s1.Branch,s1.no_of_class,s1.timing)
# print(s2.Branch,s2.no_of_class,s2.timing)



#Accessing class members using class name
# print(Qspider.Branch)
# print(Qspider.no_of_class)
# print(Qspider.timing)
# print(Qspider.timing,Qspider.no_of_class,Qspider.Branch)

#Accessing class members using object reference
# print(s1.Branch)
# print(s1.no_of_class)
# print(s1.timing)
# print(s1.timing,s1.no_of_class,s1.Branch)

# class School:
#     SNAME= 'JES'
#     LOC = 'Hampi'
#     PRINCIPAL= 'Nandakumar'
#     TIMING= '9am - 4:30pm'
# st1 = School()
# print(School.SNAME, School.LOC, School.PRINCIPAL, School.TIMING)
# print(st1.SNAME, st1.LOC, st1.PRINCIPAL, st1.TIMING)


#~-------------------------------------------------------------------------
# class Qspider:
#     Branch="Ahmedabad"
#     no_of_class=6
#     timing="10 to 8"

# s1=Qspider()
# s2=Qspider()

# s1.name="Rohit"
# s1.degree="B.Tech"
# s1.course="Python full stack"

# s2.name="Rahul"
# s2.degree="B.Tech"
# s2.course="Java full stack"

# print(s1.name,s1.degree,s1.course)
# print(s2.name,s2.degree,s2.course)

#~-------------------------------------------------------------------------

# def convert_up(s,out):
#  for i in s: 
#   if 'a'<=i<='z':
#    out += chr(ord(i)-32)
#   else:
#    out += i
#  return out 
# s="Hello"
# out=""
# print(convert_up(s,out))


#~---------------------------------------------------------------------------
