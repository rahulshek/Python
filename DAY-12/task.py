# WAP to get the following output :-
# Input: 
# "this is a test this is simple"

# Output:
# {'this': 2, 'is': 2, 'a': 1, 'test': 1, 'simple': 1}

# a="this is a test this is simple"
# out={}
# c=a.split()
# # print(c)
# for i in c:
#     if i in out:
#         out[i]+=1
#     else:
#         out[i]=1
# print(out)


#-------------------------------------------------------------------------------------

# WAP to get the following output :-
# Input list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: {0: [3, 6, 9], 1: [1, 4, 7], 2: [2, 5, 8]}

# a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# out={}
# for i in range(3):
#     out[i]=a[i::3]
# print(out)

# for i in range(3):
#     if i%3==0:
#         out[i]=a[i::3]
#     elif i%3==1:
#         out[i]=a[i::3]
#     else:
#         out[i]=a[i::3]
# print(out)