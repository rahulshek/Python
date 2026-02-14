
#& Input = PyTHONNative
#&  output =yativePTHONN

# a="PyTHONNative"
# lower=""
# upper=""
# for i in a:
#     if i.islower():
#         lower=lower+i
#     else:
#         upper=upper+i
# print(lower+upper)



#^-------------------------------------------------------------

#& input=’PyTHon’
#& output=’PTHyon’

# a="PyTHon"
# lower=""
# upper=""
# for i in a:
#     if i.islower():
#         lower=lower+i
#     else:
#         upper=upper+i
# print(lower+upper)


#^-------------------------------------------------------------

#string="P@#yn26at^&i5v”
#Chars=8
#Digits=3
#Symbol = 4
# a="P@#yn26at^&i5v"
# chars=0
# digits=0
# symbol=0
# for i in a:
#     if i.isalpha():
#         chars=chars+1
#     elif i.isdigit():
#         digits=digits+1
#     else:
#         symbol=symbol+1
# print(chars,digits,symbol)

#^----------------------------------------------------------------

# Input - ‘my name is yash patel’
# Output- ‘patel yash is name my’
# a="my name is yash patel"
# b=a.split()
# c=b[::-1]
# out=""
# for i in c:
#     out=out+i+" "
# print(out)


#^----------------------------------------------------------------

#WAP to remove to remove the duplicates from the list 

# a=eval(input("Enter a list : "))
# out=[]
# for i in a:
#     if i not in out:
#         out.append(i)
# print(out)


#^----------------------------------------------------------------

# Write a program to find largest/second largest number from the list

# a=[10,20,30,40]
# largest=0
# second_largest=0
# for i in a:
#     if i>largest:
#         if i>second_largest:
#             second_largest=largest
#             largest=i
#         else:
#             second_largest=i
# print(largest,second_largest)


#^----------------------------------------------------------------

# s=[10,20,30,25,35,40]

# b=[10,35,40]

# output=[20,30,25]

# a=[10,20,30,25,35,40]
# b=[10,35,40]
# output=[]
# for i in a:
#     if i  in b:
#         output.append(i)
# print(output)

#^----------------------------------------------------------------

#    l=[’S1001’,’S1002’,’S1003’,’S1004’]
#    h=[’Virat’,’Rohit’,’Black’,’Jhon’]
#    b=[34,33,80,60]
#    output=[{’S1001’:{’Virat’:34}},{’S1002’:{’Rohit’:33}},{’S1003’:     {’Black’:80}},{’S1004’:{’Jhon’:’60’}}]

# l=["S1001","S1002","S1003","S1004"]
# h=["Virat","Rohit","Black","Jhon"]
# b=[34,33,80,60]
# output={}
# for i,j,k in  zip(l,h,b):
#     output[i]={j:k}

# print(output)

#^---------------------------------------------------------------

#D = ['red','black','yellow']
#Output = ['c','red','c','black','c','yellow']

# d=["red","black","yellow"]
# out=[]
# for i in d:
#     out.append("c")
#     out.append(i)
# print(out)

#^---------------------------------------------------------------

#  a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23]
#     output=[2,3,5,7,11,13,17,23]
#      using advance concepts

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,23]
# out=[]

# for i in a:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             out.append(i)
# print(out)

#^---------------------------------------------------------------
# Write a python program to count how many numbers are     greater than 50 and count how many numbers are odd numbers.
# Input list: [10, 55, 42, 17, 58]
# Output: Numbers greater than 50 : 2
# Odd numbers : 3

# a=[10, 55, 42, 17, 58]
# count=0
# count1=0
# for i in a:
#     if i>50:
#         count=count+1
#     if i%2!=0:
#         count1+=1
# print("Numbers greater than 50 :", count)
# print("odd Number :", count1)


#^---------------------------------------------------------------
#  Write a python program to find the highest marks and how many students got them.
# Input: marks = {'Anuradha': 85, 'Baburao': 90, 'Totlashet': 92, 'Shyam': 92}
# output =Highest Marks =92
# Students =['Totlashet', 'Shyam']
# marks = {'Anuradha': 85, 'Baburao': 90, 'Totlashet': 92, 'Shyam': 92}
# out=[]
# highest=max(marks.values())
# # print(highest)
# for i in marks:
#     if marks[i]==highest:
#         out.append(i)
# print("Highest Marks =", highest)
# print("students =", out)


#^---------------------------------------------------------------
# Write a Python program to group numbers by their remainder when divided by 3.

# Input list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: {0: [3, 6, 9], 1: [1, 4, 7], 2: [2, 5, 8]}

# t=[1,2,3,4,5,6,7,8,9]
# out={}
# for i in t:
#     rem=i%3
#     if rem not in out:
#         out[rem]=[i]
#     else:
#         out[rem].append(i)
# print(out)

#^---------------------------------------------------------------

## Write a Python program to count how many times each word occurs in a sentence.

# ## Input Sentence:
# "this is a test this is simple"

# ## Output:
# {'this': 2, 'is': 2, 'a': 1, 'test': 1, 'simple': 1}

# a="this is a test this is simple"
# b=a.split()
# out={}
# for i in b:
#     if i not in out:
#         out[i]=1
#     else:
#         out[i]+=1
# print(out)

#^------------------------------------------------------------------------

## Write a python program to remove the duplicates from the list and add the non-duplicate values to the second list.

# ## Input:
# L1 = [1, 3, 1, 5, 2, 1, 4, 5, 6, 6, 2, 7]

# ## Output:
# L2 = [1, 2, 3, 4, 5, 6, 7]

# a=[1,3,1,5,2,1,4,5,6,6,2,7]
# out=[]
# for i in a:
#     if i not in out:
#         out.append(i)
# print(out)


#^------------------------------------------------------------------------

# Write a program to check whether the given number is prime number or not

# a=int(input("Enter a number : "))
# count=0
# if a>1:
#     for i in range(2,a):
#         if a%i==0:
#             count+=1
#             break
#     if count==0:
#      print("Prime")
#     else:
#         print("Not Prime")
# else:
#    print("We can't tell whether 1 is prime or not prime")


#^----------------------------------------------------------------------

# Write a program to check whether given number is Strong /Armstrong number or not

#for armstrong number 

# a=int(input("Enter a number : "))
# c=str(a)
# b=len(c)
# count=0
# for i in c:
#     count+=int(i)**b
# if count==a:
#     print("ArmStrong Number")
# else:
#     print("Not ArmStrong Number")

# a=int(input("Enter a number to check :"))
# sum=0
# pow=len(str(a))
# for i in str(a):
#     sum=sum+(int(i)**pow)
# if sum==a:
#     print("ArmStrong")
# else:
#     print("Not a armstrong")


# for strong number

# a=int(input("Enter a number : "))
# temp=a
# out=0
# while a> 0:
#     s=a%10
#     fact=1
#     for i in range(1,s+1):
#         fact=fact*i
#     out=out+fact
#     a=a//10

# if out==temp:
#     print("Strong Number ")
# else:
#     print("Not a strong number ")
        


#^-------------------------------------------------------------------

# Write a program to program to print prime numbers upto n

# a=int(input("Enter n number you want prime: "))
# for i in range(2,a+1):
#     fact=0
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

#^--------------------------------------------------------------------

# s=aaabbccddd
# output=a3b2c2d3

# s="aaabbccddd"
# out=""
# for i in s:
#     if i not in out:
#         out+=i+str(s.count(i))
# print(out)        
 


        
#^-----------------------------------------------------------------------

# a=24
# b=12
# c=0
# d= a or c
# e=d and b
# print(d+e)


#^------------------------------------------------------------------------

# Write a program to check whether the given list is a sublist or not

# a=[1,2,3,4,[1,2,3]]
# flag=0
# for i in a:
#     if type(i)==type(a):
#         flag=flag+1
#         break
# if flag==1:
#     print("true")
# else:
#     print("false")

#^------------------------------------------------------------------------

# Write a program to make an simple calculator
# a="yes"
# while a=="yes":
#     num1=int(input("Enter a number 1  : "))
#     num2=int(input("Enter a number 2 : "))
#     op=input("Enter a operator : ")
#     if op=="+":
#         print(num1+num2)
#     elif op=="-":
#         print(num1-num2)
#     elif op=="*":
#         print(num1*num2)
#     elif op=="/":
#         print(num1/num2)
#     else:
#         print("Invalid operator")
#     a=input("Enter your choice yes/no : ")
# print("thank You ")

#^------------------------------------------------------------------------

# Validate pin it must have 4 digits it should not have 3 continuous numbers eg.123 one digit should not repeat 3 times eg. 333

# a=int(input("Enter a pin: "))
# if a>999 and a<10000:
#     temp=str(a)
#     for i in temp:
#         if int(temp[0])!= int(temp[1])!= int(temp[2]) or int(temp[1])!= int(temp[2])!= int(temp[3]):
#             if int(temp[0])+1 != int(temp[1]) != int(temp[2])-1 or int(temp[1])+1 !=  int(temp[2]) != int(temp[3])-1:
#                 print("Valid pin")
#                 break
#             else:
#                 print("Invalid pin 3 conticutive")
#                 break
#         else:
#             print("Invalid pin becuse 3 contivvie smae nuber")
#             break       
# else:
#     print("Invalid length of pin.")

#^--------------------------------------------------------------------------------

### Write a program to print the following pattern

#           $
#       $      $
#    $     $       $





#^-------------------------------------------------------------------



#^---------------------------------------------------------------
#25 Extract and count the highest number of char from string
# a=input("Enter a string : ")
# b=0
# c=""
# for i in a:
#     digit=a.count(i)
#     if digit>b:
#         b=digit
#         c=i
# print(c,"=",b)

#^---------------------------------------------------------------


# c=eval(input("Enter a list  : "))
# count=0
# for i in range (0,len(c)):
#     if type(c[i])==str:
#         count+=1
# print(count)
        
#^----------------------------------------------------------------

# l=[’S1001’,’S1002’,’S1003’,’S1004’]
# h=[’Virat’,’Rohit’,’Black’,’Jhon’]
# b=[34,33,80,60]


# l=["S1001","S1002","S1003","S1004"]
# h=["virat","Rohit","Black","Jhon"]
# b=[34,33,80,60]


#^-------------------------------------------------------

# out={}
# for i,j,k in zip(l,h,b):
#     out[i]={j:k}
# print([out])

#^-----------------------------------------------------------
# a=[1,2,3,4,5,6,7,8,9]
# out={}
# for i in a:
#     rem=i%3
#     if rem not in out:
#         out[rem]=[i]
#     else:
#         out[rem].append(i)
# print(out)

# Input={10:’star’,20:’byee’,30:’moon’,40:’apple’}
#        Output={’star’:10,’byee’:20,’moon’:30,’apple’:40}


# a={10:"star",20:"byee",30:"moon",40:"apple"}
# out={}
# for i , j in zip (a.keys(),a.values()):
#     out[j]=i
# print(out)


# a=28
# sum=0
# for i in range(1,a):
#     if a%i==0:
#         sum+=i
# if sum==a:
#     print("perfect")
# else:
#     print("No perfect")


# * * * * *
# * * * * * 
# * * * * *
# * * * * *
# * * * * *

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
        
#             print("*",end=" ")
#     print()


# Write a program to reverse the string or reverse the number using while loop or for loop

# a="python"
# out=""
# for i in a:
#     out=i+out
# print(out)


# a=5
# sum=1
# for i in range (1,a+1):
#     sum=sum*i
# print(sum)


# Write a program to count no of occurences of a particular character in a string 

# inp="aaabbbcc"
# out=''
# count=1
# for i in range (len(inp)-1):
    
#     if inp[i]==inp[i+1]:
#         count+=1
#     else:
#         out+=inp[i]+str(count)
#         count=1
# print(out+inp[-1]+str(count))


# s="aaabbccdddaaaa"
# out=""
# for i in s:
#     if i not in out:
#         out+=i+str(s.count(i))
# print(out) 

# temp=121
# n=temp
# out=0
# while n>0:
#     s=n%10
#     out=out*10+s
#     n=n//10
# if temp==out:
#     print("yes")


