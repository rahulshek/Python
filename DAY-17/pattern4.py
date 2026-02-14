# # WAP to print the pattern :-

# A 
# A B 
# B C D
# D E F G
# G H I J K


n=5
start=65
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(chr(start), end=" ")
            start+=1
    start=start-1
    print("")
