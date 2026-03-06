
#*-----------------------------------------------------------------------------------------------

# w=['python', 'java', 'holiday', 'easy']
# # out = ['pn', 'ja', 'hy' , 'ey' ]

# func=lambda x: x[0]+x[-1]
# out=list(map(func,w))
# print(out)


#*-----------------------------------------------------------------------------------------------


# output={1:1,2:8,3:27,4:64,5:125}

# func=lambda x: x**3
# collection=list(range(1,6))
# output=dict(zip(collection,map(func,collection)))
# print(output)


#*-----------------------------------------------------------------------------------------------

#& Filter() function

#? WAP to extract only integer values from a list
# l=[12,34,6.7,True,8+9j,"Hii","hahaha"]
# out=[]
# for i in l:
#     if type(i)==int:
#         out.append(i)
# print(out)


# func=lambda x: type(x)==int
# out=list(filter(func,l))
# print(out)

# print(list(filter(lambda x: type(x)==int,l)))

#*-----------------------------------------------------------------------------------------------

#? Program to extract even numbers between the range 1 to 10

# even=list(filter(lambda x: x%2==0,list(range(1,11))))
# print(even)

#*-----------------------------------------------------------------------------------------------

#? Extract all the string values from the tuple only if it is starting with uppercase and ending with lowercase
# t = (10,2.3,'Supritha','home','pythoN','Ugadi')
# out= lambda x: type(x)==str and x[0].isupper() and x[-1].islower()
# print(list(filter(out,t)))

#*-----------------------------------------------------------------------------------------------

#? Program to find the square of all the even numbers from the given list
# l = [1.0,2,3.0,4,5.0,6]
# sqr=lambda x: x**2 if x%2==0 else x
# print(list(map(sqr,l)))

#*-----------------------------------------------------------------------------------------------   

#? Program to extract all the collection values present in a list which has even length
l = [10,2.3,'sakshi',[10,20,30],(7,8),{1,2,3,4}]

print(list(filter(lambda x: len(str(x))%2==0,l)))