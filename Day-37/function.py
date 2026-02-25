
#~----------------------Tuple_Packing------------------------------------#
# def pack(*args):
# 	print(type(args))
# 	print(args)
	 
# pack(10,20,30,40)

#~----------------------dict_packing------------------------------------#

# def dictpacking(**kwargs):
# 	print(type(kwargs))
# 	return kwargs
# print(dictpacking(name="Rahul",age=20,city="Mumbai"))

#*--------------------------------------------------------------------------------------------#

# def packing(*args,**kwargs):
# 	return args,kwargs
# print(packing(10,20,30,40,name="Rahul",age=20,city="Mumbai"))

# #!Output 
# #(10, 20, 30, 40) {'name': 'Rahul', 'age': 20, 'city': 'Mumbai'}

#*--------------------------------------------------------------------------------------------#

#~---------------------------Unpacking------------------------------------#

def unpacking(a,b,c):
	return a,b,c


print(unpacking(*[10,20,30]))
#!output
# (10, 20, 30)

print(unpacking(*{'a':10,'b':20,'c':30}))
#!output
# ('a', 'b', 'c')

print(unpacking(*'hii'))
#!output
# ('h', 'i', 'i')