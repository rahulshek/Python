#WAp to reverse the number using while loop

# a=145
# out=0
# while a>0:
#     s=a%10
#     out=out*10+s
#     a=a//10
# print(out)

#WAP to find the sum of digits of a number using while loop

# a=int(input("Enter a number: "))
# sum=0
# while a>0:
#     s=a%10
#     sum=sum+s
#     a=a//10
# print(sum)

#WAP to print factors of a numbers

# a=int(input("Enter a number you want factors : "))
# sum=0
# for i in range(1,a+1):
#     if a%i==0:
#         sum+=i
# print(sum)

#WAP to get the following output
# a="PytHON@12%" 
# upper=""
# lower=""
# special=""
# for i in a:
#     if "A"<=i<="Z":
#         upper+=i
#     elif "a"<=i<="z":
#         lower+=i
#     else:
#         special+=i
# print(upper+lower+special)

# a=input("Enter a char : ")
# if "A"<=a<="Z":
#     print(chr(ord(a)+32)) 
# elif "a"<=a<="z":
#     print(chr(ord(a)-32)) 
# elif "0"<=a<="9":
#     print(int(a)%3)
# else:
#     print(ord(a))


# a=eval(input("Enter a list : "))
# if len(a)%2!=0:
#     if type(a[len(a)//2])==str:
#         print(a[len(a)//2])


# a=input("Enter a string : ")
# if a[0] in "aeiouAEIOU":
#     if a[-1] not in "aeiouAEIOU":
#         if a[len(a)//2]=="a" or "A":
#             print(a[::-1])


# a=8
# count=0
# for j in range(2,a):
#     if a%j==0:
#         count+=1
# if count >0:
#     print("No prime")
# else:
#     print("prime")


# a=int(input("Enter lower  limit : "))
# b=int(input("Enter upper limit: "))
# out=[]
# for i in range(a,b):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count==0:
#         out.append(i)
# print(out)

# a=["hii",12,45,6+7j,True,"Holiday"]
# out=[]
# for i in a:
#     if type(i)==str:
#         for j in i:
#             if j in "aeiouAEIOU":
#                 out.append(j)
# print(out)
        
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

# a="hello this is hello python"
# b=a.split()
# out={}
# # print(b)
# for i in b:
#     if i not in out:
#         out[i]=1
#     else:
#         out[i]=out[i]+1
# print(out)

        


# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>j:
#             print("*",end="")
#         elif i==j:
#             print("$",end="")
#     print("")


# a=65
# out={}
# for i in range(65,91):
#     out[chr(i)]=i
# print(out)

# a="Python is easyi to learn"
# b=a.split()
# out={}
# for i in b:
#     if len(i)%2==0:
#         out[i]=len(i)
#     else:
#         out[i]=i[::-1]
# print(out)

# n=5
# s=65
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(chr(s),end="")
#             s=s+1

#     print("")