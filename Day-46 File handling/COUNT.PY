
# n=input("Enter the char : ")
with open("file.txt", "r") as cursor:
    entires = cursor.readlines()
#     count=0
#     for i in entires:
#         count+=i.count(n)
#     print(count)

#*------------------------------------------------------------------------------

    # n = input("Enter the char : ")
    # with open('file.txt', 'r') as cursor:

    #     data = cursor.read().split()
    #     print(len(data))

#*------------------------------------------------------------------------------

#     n = input("Enter the word : ")
#     count = 0
#     for i in entires:
#         if n in i:
#             count += 1
# print(n, "=", count)

#*-------------------------------------------------------------------------------
    

#WAP to read the contains from 2 files and merge all the content into another file named merge.txt 

# with open('file1.txt','r') as cursor:
#     data=cursor.readlines()

# with open('file2.txt','r') as cursor1:
#     data1=cursor1.readlines()

# total_data=data+data1
# with open('merge.txt','w') as cursor:
#     cursor.writelines(total_data)
#     print("Done")

#*-------------------------------------------------------------------------------

#WAP to remove all the lines that contain ch  'a' in the file and write that data into another file named result.txt

# with open("file1.txt",'r') as cursor:
#     result=[]
#     data=cursor.readlines()
#     for i in data:
#         if 'a' not in i and 'A' not in i:
#             result.append(i)
# with open("result.txt",'w') as cursor:
#     cursor.writelines(result)
#     print("Done")

#*-------------------------------------------------------------------------------

# with open("file1.txt",'r+') as cursor:
#     data=cursor.read()
# #     cursor.write("I am from r+ mode of operation\n")
#     print(len(data))
#     print(cursor.tell())
#     print("Done")

#*-------------------------------------------------------------------------------

with open('feature.txt','w+') as cursor:
    cursor.write("Dynamically Typed Language\nsimple syntax\nEasy to learn\nplatform independent\n")
    cursor.seek(0)
    data=cursor.read()
    print(data)