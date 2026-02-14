#WAP to print the pattern :-

"""
65 
66 67 
68 69 70
71 72 73 74
75 76 77 78 79

"""
n=5
start=65
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(start, end=" ")
            start+=1
    start=start-1
    print("")


#WAP to print the following pattern:
""" 
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
 """
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(j, end=" ")
    print("")
