#WAP to print prime number upto N

# num=int(input("Enter a limit till where you want to print prime numbers: "))
# out=[]
# for k in range(2,num+1):
#         count=0
#         for i in range(2,k):
#             if k%i==0:
#                 count=count+1
#         if count==0:
#             out.append(k)
# print(out)

#----------------------------------------------------------------------------------------

#WAP to print perfect number upto N
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

#----------------------------------------------------------------------------------------

# a={ "star" : 10 , "byee" : 30 , "moon": 80 }
# d={}
# for i in a:
#     d[a[i]]=i
# print(d)