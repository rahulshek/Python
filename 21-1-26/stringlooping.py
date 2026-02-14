# WAP to get the following output:-
# h=”abcabacbcc”
# out=”a3b3c4”

# h="abcabacbcc"
# out=""
# count=0
# for i in h :
#     if i not in out:
#         out=out+i
#         count=h.count(i)
#         out=out+str(count)
# print(out)


#---------------------------------------------------------------------------------------

# WAP to get the following output:-
# input = “aaabbaabcc”
# output = “a3b2a2b1c2

# h="aaabbaabcc"
# out=""
# count=1
# for i in range(len(h)-1) :
#     current=h[i]
#     next=h[i+1]
#     if current==next:
#         count+=1
#     else:
#         out=out+current+str(count)
#         count=1
# print(out+current+str(count))


#------------------------------------------------------------------------

# WAP to find the highest marks and how many students got them.
# Input :  marks={ “Anuradha “ :85 ,”Baburoa”, :90 , “Totlashet” : 92 , “Shyam” : 92 }
# Output:  Highest Mark = 92
#          Students = [ “Totlashet” , “Shyam” ]

marks={ "Anuradha " :85 , "Baburoa" :90 , "Totlashet" : 92 , "Shyam" : 92 }
max=0
student=[]
for i in marks:
    if marks[i]>max:
        max=marks[i]
for i in marks:
    if marks[i]==max:
        student.append(i)
print("Highest Mark =",max)
print("Students =",student)