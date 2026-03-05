
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