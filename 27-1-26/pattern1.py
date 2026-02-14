#WAP to print the pattern 

""" 
1
1 2
2 3 4
4 5 6 7
7 8 9 10 11

 """
n=5
start=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(start, end=" ")
            start+=1
    start=start-1
    print("")