
# out={1:1,2:4,3:9,4:16,5:25}

# a={i:i**2 for i in range(1,6)}
# print(a)

# z="Hii hello tommorow is Sunday Manav"
# # out={'hii':3,'hello':5,'manav':5}
# a={i:len(i) for i in z.split() if len(i)%2!=0}
# print(a)

# a=['nayan','abcd','data','appa']
# # # out={'nayan':5,'abcd':'dcba','data':'atad','appa':'appa'}
# b={i:len(i) if i==i[::-1] else i[::-1]for i in a}
# print(b)

# a=[1,2,3]
# b=[4,5,6]
# # output = {1: 4, 2: 5, 3: 6}
# out={i:j for i,j in zip(a,b)}
# print(out)

#*-------------------------------------------------------------------------------------------------


# #From string "Python" , create a dictionary where key = character, value = ASCII value
# a='Python'
# # out={'P':80,'y':121,'t':116,'h':104,'o':111,'n':110}
# b={i:ord(i) for i in a}
# print(b)


#*-------------------------------------------------------------------------------------------------

# Given nums = [10, -5, 8, -3, 0, 12] , create a dictionary with key = number,value = "Positive" only for positive numbers

# a=[10, -5, 8, -3, 0, 12]
# b={i:'Positive' for i in a if i>0}
# print(b)

#*-------------------------------------------------------------------------------------------------

# # Get the following output
# a= ["Apple", "Banana", "Cherry", "Dates","Orange","Ice apple"]
# # output={'Apple':"A","Banana":"b","Cherry":"c","Dates":"D","Orange":"o","Iceapple":"I"}

# b={i:i[0] if len(i)%2!=0 else i[0].lower() for i in a}
# print(b)

#*-------------------------------------------------------------------------------------------------

# #  Get the following output
# a=['Anaya','Rohit','Sneha','Aarav','Meera']
# b=[85, 72, 90, 67, 88]
# # find average marks, then create a dictionary {name: "Above Avg" or "Below Avg"}
# # output={'Anaya':"Above Avg",'Rohit':"Above Avg",'Sneha':"Above Avg",'Aarav':"Below Avg",'Meera':"Above Avg"}
# b={i:'Above Avg' if j>sum(b)/len(b) else 'Below Avg' for i,j in zip(a,b)}
# print(b)

#*-------------------------------------------------------------------------------------------------

# # From the string "programming" , count occurrences of each character using dictionary comprehension.
# a="programming"
# b={i:a.count(i) for i in a}
# print(b)

#*--------------------------------------------------------------------------------------------------

# Get the following output
# s= "python is fun and python is easy”
# output={'python':2, 'is':2, 'fun':1, 'and':1, 'easy':1}
# s="python is fun and python is easy"
# a={i:s.count(i) for i in s.split()}
# print(a)                

# wap TO MOVE ALL THE ZERO AT THE END OF LIST 
# a=[0,1,2,0,3,4,0,5,6,7,8,0,9]
# b=[i for i in a if i!=0]+[i for i in a if i==0]
# print(b)
a=[0,1,2,0,3,4,0,5,6,7,8,0,9]

pos=0
for i in range(len(a)):
    if a[i]!=0:
        a[pos],a[i]=a[i],a[pos]
        pos+=1
print(a)




# for i in a:
#     if i==0:
#         a.remove(i)
#         a.append(i)
# print(a)

