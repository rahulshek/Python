# num=int(input("Enter a number: "))

# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

# choice=10
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)
#     print(10*'-')
#     print("\n")


# WAP to print sum of factorial of numbers upto n
# num=int(input("Enter a number: "))
# sum=0
# for i in range(1,num+1):
#     fact=1
#     for j in range(1,i+1):
#         fact=fact*j
#     sum=sum+fact
# print(num,"is",sum)



# WAP to extract only vowels  from the given list 
# a=[12,3.4,”Holiday” , True, “apple , 8+9j]

# a=[12,3.4,"Holiday" , True, "apple", 8+9j]
# out=[]
# for i in a:
#     if type(i)==str:
#         for j in i:
#             if j in "aeiouAEIOU":
#                 out.append(j)
# print(out)

# WAP to  extract only prime number from the given list 
# a=[ 12 ,67,89,23,45,3,13,17,19 ]

# a=[ 12 ,67,89,45,3,13,17,20 ]
# out=[]
# count=0
# for i in a:
#     for j in range(2,i):
#         if i%j==0:
#             count=count+1
#     if count==0:
#         out.append(i)
#     count=0
# print(out)

#-----------------------------------------------------------


#WAP to print wheter number is a strong number or not 
# num=int(input("Enter a number: "))
# temp=str(num)
# sum=0
# for i in temp:
#     fact=1
#     for j in range(1,int(i)+1):
#         fact=fact*j
#     sum=sum+fact
# if sum==num:
#     print(num,"is a strong number")
# else:
#     print(num,"is not a strong number")


#------------------------------------------------------------


#WAP tp check whether the given number is armstrong or not

# num=int(input("Enter a number: "))
# c=len(str(num))
# temp=num
# sum=0
# for i in range(1,c+1):
#     a=num%10
#     sum=sum+(a**c)
#     num=num//10
# if sum==temp:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

#------------------------------------------------------------

#WRITE A PROGRAM PRINT STRONG NUMBERS UPTO N
# start=int(input("Enter a start number: "))
# num=int(input("Enter a end numnber: "))
# out=[]
# for i in range(start,num+1):
#     temp=str(i)
#     sum=0
#     for j in temp:
#         fact=1
#         for k in range(1,int(j)+1):
#             fact=fact*k
#         sum=sum+fact
#     if sum==int(i):
#         out.append(i)
# print(out)


#------------------------------------------------------------

# a=[1,2,3,4]
# out=[]
# for i in range(len(a)-1):
#     # digit=i
#     res=a[i]**a[i+1]
#     out.append(res)

# print(out)


#------------------------------------------------------------

