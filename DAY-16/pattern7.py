#WAP to print the pattern :-
""" 
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1

"""


n=int(input("Enter the number of rows : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=n+1:
            print(j,end=" ")
      
    print()