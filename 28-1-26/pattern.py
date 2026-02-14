#WAp to print the following pattern:-

""" 
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *

 """

# n=int(input("Enter No rows : "))
# for i in range(1,n+1):
#     for s in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i*2):
#         print("*",end=" ")
#     print()



#-----------------------------------------------------

#WAP to print the following pattern:-

"""
    * * * * * * * * * * 
      * * * * * * * * 
        * * * * * * 
          * * * * 
            * * 
              * 
"""

# n=int(input("Enter No rows : "))
# for i in range(1,n+1):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,(n-i+1)*2):
#         print("*",end=" ")
#     print()



#-------------------------------------------------

#WAP to print the pattern
""" 
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

 """

# n=5
# for i in range(1,n):
#     for s in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i*2):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,(n-i+1)*2):
#         print("*",end=" ")
#     print()



#--------------------------------------------------
""" 
       1 
      1 2 3 
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
"""

# n=5
# for i in range(1,n+1):
#     for s in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i*2):
#         print(j,end=" ")
#     print()


#-------------------------------------------------

"""  
        A 
      A B C 
    A B C D E
  A B C D E F G
A B C D E F G H I
 
 """

n=5
for i in range(1,n+1):
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i*2):
        print(chr(65+j-1),end=" ")
    print()