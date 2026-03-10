
# n=input("Enter the char : ")
with open("file.txt", "r") as cursor:
    entires = cursor.readlines()
#     count=0
#     for i in entires:
#         count+=i.count(n)
#     print(count)

# *------------------------------------------------------------------------------

    # n = input("Enter the char : ")
    # with open('file.txt', 'r') as cursor:

    #     data = cursor.read().split()
    #     print(len(data))

# *------------------------------------------------------------------------------
    n = input("Enter the word : ")
    count = 0
    for i in entires:
        if n in i:
            count += 1
print(n, "=", count)

#*-------------------------------------------------------------------------------
    

#WAP to read the contains from 2 files and merge all the content into another file named merge.txt 

#WAP to remove all the lines that contain ch  'a' in the file and write that data into another file named remove.txt