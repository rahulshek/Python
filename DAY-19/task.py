
#& WAP to extract the vowels from a given list only if length of the string is odd

# list=[12,3.4,True,"hii",3+9j,"even"]
# out=[]
# for i in list:
#     if type(i)==str and len(i)%2!=0:
#         for j in i:
#             if j in "aeiouAEIOU":
#                 out.append(j)
# print(out)

#^--------------------------------------------------------------------------------

#& WAP to extract only prime numbers from the given list
#? a=[12,56,3,7,67,45,55,90]

# a=[12,56,3,7,67,45,55,90]
# out=[]
# for i in a:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             out.append(i)
# print(out)

#^--------------------------------------------------------------------------------

#& WAP to check whether the given list is containing a nested list or not

l=[12,3.4,True,"hii",3+9j,[1,2,3]]
# l=[12,3.4,True,"hii",3+9j]
for i in l:
    if type(i)==list:
        print("List have nested list")
        break
else:
    print("perfect list")
