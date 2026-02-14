
#& Wapp to check if a given list is homogeneous or heterogeneous 

# a=eval(input("Enter the list : "))
# s=type(a[0])
# # print(s)
# for i in a:
#     if type(i)!=s:
#         print("Heterogeneous")
#         break
# else:
#     print("Homogeneous")

#& wapp to check tf a given number is prime or not 
# a=int(input("Enter the number to check prime or not : "))
# count=1
# for i in range(2,a-1):
#     if a%i==0:
#         count+=1
# if count==1:
#     print("Prime")
# else:
#     print("Not Prime")

#& wapp to check if a given nuber is strong or not 

# a=input("Enter a number to check whether strong or not : ")
# sum=0
# for i in a:
#     digit=int(i)
#     fact=1
#     for j in range(1,digit+1):
#         fact*=j
#     sum+=fact
# if sum==int(a):
#     print("Strong")
# else:
#     print("Not Strong")




#& wapp to check if a given number is Armstrong or not 
# a=input("Enter a number to check whether Armstrong or not : ")
# sum=0
# for i in a:
#     digit=int(i)
#     sum+=digit**len(a)
# if sum==int(a):
#     print("Armstrong")
# else:
#     print("Not Armstrong")
#& WAPP to group the numbers by thier remainder when divided by 3 (eg. {0:[3,6,9], 1:[1,4,7]})

# input=[1,2,3,4,5,6,7,8,9]
# output={0:[3,6,9], 1:[1,4,7], 2:[2,5,8]}
# t=[1,2,3,4,5,6,7,8,9]
# out={}
# for i in t:
#     rem=i%3
#     if rem not in out:
#         out[rem]=[i]
#     else:
#         out[rem].append(i)
# print(out)
    
#& WAPP to remove the duplicates from the list and add the non-duplicate values to the second list (e.g  l = [1,3,1,5,2,1,4,5,6,6,2,7] ---> output =[3,4,7]  )33
# input=[1,3,1,5,2,1,4,5,6,6,2,7]
# output=[3,4,7]
# l=[1,3,1,5,2,1,4,5,6,6,2,7]
# out=[]
# for i in l:
#     if l.count(i)==1:
#         out.append(i)
# print(out)

#& WAP to find second largest in list 
# s=eval(input("Enter a list :"))
# a=set(s)
# largest=0
# s_largest=0
# for i in a:
#     if i>s_largest:
#         if i >largest: 
#             s_largest=largest
#             largest=i
#         else:
#             s_largest=i
# print(s_largest,"it is a second largest in list ")

#& WAP Array is sorted or not 

# array=eval(input("Enter a list to check whether sorted or not :"))
# # array=[1,2,3,4,5]
# out=0
# for i in range(0,len(array)-2):
#     if array[i]>array[i+1]:
#         out+=1
#         break
# if out==0:
#     print("Sorted")
# else:
#     print("Not Sorted")