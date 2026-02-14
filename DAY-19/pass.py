# #WAP to used the pass statement

# for i in  range(1,5):
#     pass

#& WAP to extract the vowels from a given list only if length of the string is odd


list=[12,3.4,True,"hii",3+9j]
out=[]
for i in list:
    if type(i)==str and len(i)%2!=0:
        for j in i:
            if j in "aeiouAEIOU":
                out.append(j)
print(out)


            