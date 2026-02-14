
#& zip function in python

#? zip function is used to combine two or more lists into a list of tuples.

#& WAP to combine two lists into a dictionary.
# students = ['smit', 'dhruv', 'rahul']
# marks = [90, 85, 55]
# out={}
# for i,j in zip(students, marks):
#     out[i]=j
# print(out)

#^-----------------------------------------------------------------------


# students=["rahul","dev","arth","smit","dhruv"]
# marks=[-9,85,101,88]
# colls=[1,2,3]
# for i,j,k in zip(students,marks,colls):
#     print(i,j,k)

#^-----------------------------------------------------------------------

#& WAP to print out={'A':65,'B':66,'C':67,...............,"Z":90 } using zip function.

# out={}
# for i,j in zip(range(65,91),range(65,91)):
#     out[chr(i)]=j
# print(out)

#^-----------------------------------------------------------------------



# d=[{'tesla':{'model':'x','colour':'black'}},{'audi':{'model':'a','colour':'red'}}]   
# out=[]
# # for i in d:
# #     for j in i:
# #         for k,v in j.items():
# #             out.append(v)
# # print(out)

# for i in d:
#     for j in i:
#         out.append(i[j])
# print(out)



a={'rahul':20}
print(a.items())

#^-------------------------------------------------------------------------------------------------