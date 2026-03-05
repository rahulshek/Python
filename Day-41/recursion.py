
# n=int(input("Enter a number till you want serires : "))  # 0 1 1 2 3
# first=0
# second=1
# print(first)
# print(second)
# while n-2>0:
#     c=first+second
#     print(c)
#     first=second
#     second=c
#     n=n-1


# #? Convert the above code in recursion

# def fibonacci(n,first=0,second=1):
#     if n<=0:
#         return
#     print(first)
#     fibonacci(n-1,second,first+second)

# fibonacci(5)

# ? WAP to print fibonacii number upto nth term
# n=int(input("Enter a number till you want serires : "))  # 0 1 1 2 3
# first=0
# second=1
# print(first)
# print(second)
# while n-2>0:
#     c=first+second
#     print(c)
#     first=second
#     second=c
#     n=n-1

# n=int(input("Enter a number till you want serires : "))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     a,b=b,a+b


# *---------------------------------------------------------------------------------------------

# reverse the number by while loop

# a=int(input("Enter a digit to reverse the number : "))
# rev=0
# while a>0:
#     rem=a%10
#     rev=rev*10+rem
#     a=a//10

# print(rev)

# for i in range(0,len(str(a))):
#         rem=a%10
#         rev=rev*10+rem
#         a=a//10
# print(rev)

# print(str(a)[::-1])


# *---------------------------------------------------------------------------------------------

# Move all the zeros in to list append

a = [0, 1, 0, 3, 12]
# cont=0
# out=[]
# for i in a:
#     if i==0:
#         cont=cont+1
#     else:
#         out.append(i)
# for i in range(cont):
#     out.append(0)
# print(out)

# for i in range(len(a)):
#     if a[i]==0:
#         a.remove(a[i])
#         a.append(0)
# print(a)

# ? WAP to check whether the given number is balance number or not

# & Sum of the digit to the left of the middle digit is equal to the sum of the digit to the right of the middle digit
# n = int(input("Enter a number : "))
# left = 0
# right = 0
# mid = len(str(n))//2

# if len(str(n)) % 2 != 0:
    
    
#     for i in range(mid):
#         left = left+int(str(n)[i])
#     for i in range(mid+1, len(str(n))):
#         right = right+int(str(n)[i])
#     if left == right:
#         print("Balance number")
#     else:
#         print("Not a balance number")
# else:
#    for i in range(mid):
#        left = left+int(str(n)[i])
#    for i in range(mid, len(str(n))):
#        right = right+int(str(n)[i]) 
#    if left == right:
#        print("Balance number")
#    else:
#        print("Not a balance number")
#*------------------------------------------------------------------------------------------------


#?WAP to print prime number upto n term
# n=int(input("Enter the range tull you want prime number : "))

# for i in range(2,n+1): # 2 3 4 5 6 7 8
#     for j in range(2,(i//2)+1): 
#         if i%j==0:
#             break
#     else:
#         print(i)
#*------------------------------------------------------------------------------------------------
# #? WAP to print the factorial of a number
# n=int(input("Enter a number to find the factorial : "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
#*------------------------------------------------------------------------------------------------