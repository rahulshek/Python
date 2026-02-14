#WAP to print 1 to 10 using while loop
# i=1
# while i<=10:
#     print(i)
#     i=i+1

#----------------------------------------------------------------------------

#WAP to print from 10 down 1 in reverse order 
# i=10
# while i>=1:
#     print(i)
#     i=i-1

#----------------------------------------------------------------------------

#WAP to print even numbers from 1 to 100
# i=1
# while i<=100:
#     if i%2==0:
#         print(i)
#     i=i+1

#----------------------------------------------------------------------------

#WAP to print odd numbers from 1 to 100
# i=1
# while i<=100:
#     if i%2!=0:
#         print(i)
#     i=i+1

#----------------------------------------------------------------------------

#WAP to print table of a given number in for n * 1 to n * 10
# num=int(input("Enter a number: "))
# i=1
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i=i+1

#----------------------------------------------------------------------------

#WAP to calculate and print rhe sum of the first natural number 
# num=int(input("Enter a number: "))
# i=1
# sum=0
# while i<=num:
#     sum=sum+i
#     i=i+1
# print("The sum of first",num,"natural numbers is",sum)

#----------------------------------------------------------------------------


#WAP to calculate and print the sum of all even number from 1  upto n 
# num=int(input("Enter a number: "))
# i=1
# sum=0
# while i<=num:
#     if i%2==0:
#         sum=sum+i
#         # print(i)
#     i=i+1
# print("The sum of all even numbers upto",num,"is",sum)

#----------------------------------------------------------------------------

#WAP to sum all the odd numbers from 1 up to n
# num=int(input("Enter a number: "))
# i=1
# sum=0
# while i<=num:
#     if i%2!=0:
#         sum=sum+i
#         # print(i)
#     i=i+1
# print("The sum of all odd numbers upto",num,"is",sum)

#----------------------------------------------------------------------------

#WAP to calculate and print the factorial of a given number
# num=int(input("Enter a number: "))
# i=1
# fact=1
# while i<=num:
#     fact=fact*i
#     i=i+1
# print("The factorial of",num,"is",fact)

#----------------------------------------------------------------------------

#WAP find and print the product of all digit of a given number
# num=int(input("Enter a number: "))
# sum=1
# digit=0
# while num>0:
#     digit=num%10
#     sum=sum*digit
#     num=num//10
# print("The product of all digits of the given number is",sum)

#----------------------------------------------------------------------------

#wap to count and print the total number of digits in a given number
# num=int(input("Enter a number: "))
# count=0
# while num>0:
#     num=num//10
#     count=count+1
# print("The total number of digits in the given number is",count)


#----------------------------------------------------------------------------

#WAP reverse the given number and print the revesed value
# num=int(input("Enter a number: "))
# rev=0
# while num>0:
#     a=num%10
#     rev=rev*10+a
#     num=num//10
# print("The reversed number is",rev)



#----------------------------------------------------------------------------

#WAP to check whether the given number is palindrome or not
# num=int(input("Enter a number: "))
# rev=0
# temp=num
# while num>0:
#     a=num%10
#     rev=rev*10+a
#     num=num//10
# # print(rev)
# if rev==temp:
#     print("The given number is palindrome")
# else:
#     print("The given number is not palindrome")


#----------------------------------------------------------------------------

#WAP to  find and print the sum of digit of the give number 
# num=int(input("Enter a number: "))
# sum=0
# while num>0:
#     a=num%10
#     sum=sum+a
#     num=num//10
# print("The sum of digits of the given number is",sum)


#----------------------------------------------------------------------------

#WAP tp check whether the given number is armstrong or not
# num=int(input("Enter a number: "))
# c=len(str(num))
# temp=num
# # print(c)
# sum=0
# while num>0:
#     a=num%10
#     sum=sum+(a**c)
#     num=num//10
# # print(sum)
# if temp == sum:
#     print("The given number is armstrong")
# else:
#     print("The given number is not armstrong")


#----------------------------------------------------------------------------

#WAP to check whether the given number is perfect or not

# num=int(input("Enter a number:"))
# i=1                         
# sum=0                       
# while i<num:
#     if num%i==0:            
#          sum=sum+i          
#     i+=1                    
# if sum==num:                
#     print("Perfect number")
# else:
#     print("Not a Perfect number")


#----------------------------------------------------------------------------

#WAP print all the prime number from 1 to 100
# i=1
# while i<=100:


#----------------------------------------------------------------------------

#WAP to print the fibonacci series upto n terms
# num=int(input("Enter a number: "))
# a=0
# b=1
# i=3
# print(a)
# print(b)
# while i<=num:
#     c=a+b
#     a=b
#     b=c
#     print(c)
#     i=i+1


#----------------------------------------------------------------------------

#WAP to find and print the sum of all the fibonacii upto n
# num=int(input("Enter a number: "))
# a=0
# b=1
# i=3
# sum=1
# print(a)
# print(b)
# while i<=num:
#     c=a+b
#     a=b
#     b=c
#     print(c)
#     sum=sum+c
#     i=i+1
# print("The sum of all fibonacci upto",num,"is",sum)


#----------------------------------------------------------------------------


#WAP to print square of each numbner from 1 to n
# num=int(input("Enter a number: "))
# i=1
# while i<=num:
#     print(i," Square is : ",i**2)
#     i=i+1


#----------------------------------------------------------------------------

#WAP to print the cube of each number from 1 to n

# num=int(input("Enter a number: "))
# i=1
# while i<=num:
#     print(i," Square is : ",i**3)
#     i=i+1


#----------------------------------------------------------------------------


#WAP to print all the number between a and b that are divisivle by 7

# num1=int(input("Enter the lower range : "))
# num2=int(input("Enter the higher range : "))
# i=num1
# while i<=num2:
#     if i%7==0:
#         print(i)
#     i=i+1


#----------------------------------------------------------------------------


#WAP all factor of the given number 
# num=int(input("Enter a number: "))
# c=[]
# i=1
# while i<=num:
#     if num%i==0:
#         c.append(i)
#     i=i+1
# print(c)


#----------------------------------------------------------------------------

#WAP to print all sum of factor of a given number

# num=int(input("Enter a number: "))
# c=0
# i=1
# while i<=num:
#     if num%i==0:
#         c=c+i
#     i=i+1
# print(c)


#----------------------------------------------------------------------------

#WAP to find the HCF( Highest Common Factor) of two given numbers

# num1=int(input("Enter a number 1 : "))
# num2=int(input("Enter a number 2 : "))
# a=[]
# b=[]
# i=1
# n=1
# while i<=num1:
#     if num1%i==0:
#         a.append(i)
#     i=i+1
# while n<=num2:
#     if num2%n==0:
#         b.append(n)
#     n=n+1
# print(a)
# print(b)


# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=[]
# d=[]
# e=[]
# for i in range(1,a+1):
#     if a%i==0:
#         c.append(i)
# print(c)
# for i in range(1,b+1):
#     if b%i==0:
#         d.append(i)
# print(d)
# for i in c:
#     if i in d:
#         e.append(i)
# print(e[-1])



#---------------------------------------------------------------------------------

#WAP to find the LCM( Lowest Common Multiple) of two given numbers

# num1=int(input("Enter a number 1 : "))
# num2=int(input("Enter a number 2 : "))
# a=[]
# for i in range(1,num1+1):
#     if num1%i==0:
#         a.append(i)
# print(a)   


#---------------------------------------------------------------------------------

#WAP to find the smallest digit in the given number 


