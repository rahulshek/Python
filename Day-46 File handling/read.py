
with open('file.txt','r') as cursor:
    # var = cursor.read()
    # print(var,type(var))

#*--------------------------------------------------------------------------------------

    # line1=cursor.readline()
    # print(line1)
    # line2=cursor.readline()
    # print(line2)
    # line3=cursor.readline()
    # print(line3)
    # line4=cursor.readline()
    # print(line4)
    # line5=cursor.readline()
    # print(line5)
    # line6=cursor.readline()
    # print(line6)

#*--------------------------------------------------------------------------------------

    entires = cursor.readlines()
    # print(entires)

#*--------------------------------------------------------------------------------------

# WAP to count number of times a particular character is repeated in the txt file
    out={}
    for i in entires:
        for j in i:
            if j in out:
                out[j]+=1
            else:
                out[j]=1
print(out)

# n=input("Enter a character to count: ")
# count=0
# for i in entires:
#     for j in i:
#         if j==n:
#             count+=1