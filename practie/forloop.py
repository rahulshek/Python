# # 1.Generate Fibonacci series up to n term
# # n=int(input("Enter the number"))
# # first=0
# # second=1
# # for i in range(n):
# #     print(first)
# #     temp=first
# #     first=second
# #     second=temp+first

# #*--------------------------------------------------------------------------------------------

# # 2. WAP to print the following output 
# # input -> 'roses are red' 
# # output -> ['sesor',3,'der']
# # s='roses are red'
# # s1=s.split()
# # s2=[]
# # for i in range(len(s1)):
# #     if i%2==0:
# #         s2.append(s1[i][::-1])
# #     else:
# #         s2.append(len(s1[i]))
# # print(s2)

# #*--------------------------------------------------------------------------------------------

# # 3. WAP to count total number of words in a string without using inbuilt methods
# # a="hi this is python programming"
# # count=1
# # for i in a:
# #     if i==" ":
# #         count+=1
# # print(count)

# #*---------------------------------------------------------------------------------------------

# # 4. WAP to convert string to upper case using for loop
# # s="python programming"
# # s1=""
# # for i in s:
# #     if i.islower():
# #         s1=s1+i.upper()
# #     else:
# #         s1=s1+i
# # print(s1)

# #*--------------------------------------------------------------------------------------------

# # 5. WAP to convert the string into title without using inbuilt functions
# # s="Python programming"
# # s1=""
# # for i in s:
# #     if i==" ":
# #         s1=s1+" "
# #     elif "A"<i<"Z":
# #         s1=s1+i
# #     else:
# #         s1=s1+chr(ord(i)-32)
# # print(s1)

# #*--------------------------------------------------------------------------------------------

# # 6. Write a program to guess the correct number
# # import random
# # n=random.randint(1,10)
# # while True:
# #     guess=int(input("Enter the number"))
# #     if guess==n:
# #         print("You guessed it right")
# #         break
# #     elif guess>n:
# #         print("You guessed it wrong, try a smaller number")
# #     else:
# #         print("You guessed it wrong, try a larger number")

# #*--------------------------------------------------------------------------------------------

# # 8. WAP print the sum of even-position and odd-position digits separately

# # a=[1,2,3,4,5,6,7,8,9]
# # even=0
# # odd=0
# # for i in range(len(a)):
# #     if i%2==0:
# #         even+=a[i]
# #     else:
# #         odd+=a[i]
# # print(even,odd)

# #*---------------------------------------------------------------------------------------------

# # 9. WAP to extract all even integers numbers present at odd index from given heterogenous list

# # a=[1,2,3,4,"Hii","Hello",True]
# # out=[]
# # for i in range(len(a)):
# #     if i%2!=0 and type(a[i])==int:
# #         out.append(a[i])
# # print(out)

# #*---------------------------------------------------------------------------------------------
        
# # 10.Check whether the given number is prime or not using intermediate termination and for loop

# # n=int(input("Enter the number"))
# # for i in range(2,n):
# #     if n%i==0:
# #         print("Not prime")
# #         break
# # else:
# #     print("Prime")

# #*---------------------------------------------------------------------------------------------

# # 11.Write a program to print table  upto n

# # n=int(input("Enter the number"))
# # for i in range(1,n+1):
# #     for j in range(1,11):
# #         print(i,"*",j,"=",i*j)

# #*---------------------------------------------------------------------------------------------

# # 12. WAP to extract only vowels from the given list of words
# # s=['Python',57,'Hii',9+8j,False,’Saturday’]

# # s=['Python',57,'Hii',9+8j,False,'Saturday']
# # out=[]
# # for i in s:
# #     if type(i)==str:
# #         for j in i:
# #             if j in "aeiouAEIOU":
# #                 out.append(j)
# # print(out)

# #*---------------------------------------------------------------------------------------------

# # 13.Write a program to sum of  factorial of individual digit

# # s=133
# # output=13
# # s=int(input("Enter the number : "))
# # out=0
# # # while s>0:
# # #     rem=s%10
# # #     fact=1
# # #     for i in range(1,rem+1):
# # #         fact*=i
# # #     out+=fact
# # #     s=s//10
# # # print(out)
# # for i in str(s):
# #     fact=1
# #     for j in range(1,int(i)+1):
# #         fact*=j
# #     out+=fact
# # print(out)

# #*--------------------------------------------------------------------------------------------

# # 14.Write a program to print prime numbers upto n

# # n=int(input("Enter the number : "))
# # for i in range(2,n+1):
# #     flag=0
# #     for j in range(2,i):
# #         if i%j==0:
# #             flag=1
# #             break
# #     if flag==0:
# #         print(i)

# #*--------------------------------------------------------------------------------------------

# # 15. Write a program to print perfect numbers upto n

# # n=int(input("Enter the number : "))
# # for i in range(2,n+1):
# #     sum=0
# #     for j in range(1,i):
# #         if i%j==0:
# #             sum+=j
# #     if sum==i:
# #         print(i)
    
# #*--------------------------------------------------------------------------------------------

# # 16. Write a program to print  STRONG NUMBER upto n

# # n=int(input("Enter the number : "))
# # for i in range(2,n+1):  
# #     sum=0
# #     temp=i
# #     while temp>0:
# #         rem=temp%10
# #         fact=1
# #         for j in range(1,rem+1):
# #             fact*=j
# #         sum+=fact
# #         temp=temp//10
# #     if sum==i:
# #         print(i)

# #*--------------------------------------------------------------------------------------------

# # 17. Write a program to print  ARMSTRONG NUMBER upto n

# # a=200
# # sum=0
# # for i in str(a):
# #     sum+=int(i)**len(str(a))
# # if sum==a:
# #     print("Armstrong")
# # else:
# #     print("Not Armstrong")

# #*--------------------------------------------------------------------------------------------

# # 18. Input : [12, 'program',4+2j, False,'holiday']
# #    Output : {'program' : 'oa', 'holiday' : 'oia'}

# s=[12, 'program',4+2j, False,'holiday']
# d={}
# for i in s:
#     if type(i)==str:
#         out=""
#         for j in i:
#             if j in "aeiouAEIOU":
#                 out+=j
#         d[i]=out
# print(d)

# #*---------------------------------------------------------------------------------------------

# # 19.Write a python program to print only those elements from the list which are  prime numbers

# # a=[10,11,12,13 ,14,15]

# a=[10,11,12,13 ,14,15]
# out=[]
# for i in a:
#     if i>1:
#         flag=0
#         for j in range(2,i):
#             if i%j==0:
#                 flag=1
#                 break
#         if flag==0:
#             out.append(i)
# print(out)

#*-----------------------------------------------------------------------------------------------

# 20. Write a program to print the sum of digits of a number using for loop
a=123
sum=0
for i in str(a):
    sum+=int(i)
print(sum)


#*-----------------------------------------------------------------------------------------------