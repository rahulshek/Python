#WAP to take input as 'HoLiDaY' and convert it to 'hOlIdAy' using for loop.
# a='HoLiDaY'
# b=''
# for i in a:
#     if 'A'<=a[i]<='Z':
#         b=b+(a[i]+32)

#WAP to print n number where n is input by user using for loop.
# n=int(input("Enter a number: "))
# for i in range(2,n,2):                 #for loop to print even numbers from 2 to n.
#     print(i)

# for i in range (2,n+1):
#     if i%2==0:
#         print(i)

#WAP to reverse the string using for loop
# ch=input("Enter a string: ")
# out=""
# for i in ch:    #for loop to reverse the string.
#     out=i+out   #to store reversed string.
# print(out)

# num=int(input("Enter a number: "))
# temp=str(num)         #to store number as string.
# out=""
# for i in temp:        #for loop to reverse the number.
#     out=i+out         #to store reversed number.
# out=int(out)          #to convert reversed number to integer.
# print(out)

#WAP to check if a given number is prime number or not using for loop.

# num=int(input("Enter a number: "))  
# count=0
# for i in range(2,num-1):               #for loop to check if a given number is prime number or not.
#     if num%i==0:                       #if condition to check if a given number is prime number or not.
#         count+=1
# if count==0:                          #if condition to check if a given number is prime number or not.
#     print("Prime :",num)
# else:                                  #else condition to check if a given number is prime number or not.
#     print("Not Prime :",num)


#WAP to check if a given number is perfect number or not using for loop
# num=int(input("Enter a number: "))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# if sum==num:
#     print("Perfect Number ",num)
# else:
#     print("Not Perfect Number ",num)


#WAP to extract present at odd index from string .
# n=input('enter a string: ')
# out=''
# for i in range(len(n)):
#     if (i%2!=0):
#         out=out+n[i]
# print(out)

# n='HoLIdaY'
# out=''
# for i in n:
#     if 'A'<=i<='Z':
#         out=out+chr(ord(i)+32)
#     elif 'a'<=i<='z':
#         out=out+chr(ord(i)-32)
#     else:
#         print('error')
# print(out)

# n=input('enter a string: ') #  Commented out: This line would prompt user to enter a string
# out=''
# for i in n: #  Iterate through each character in string n
#     if 'a'<=i<='z': #       Check if the character is a lowercase letter
#         if ord(i)%2==0: #           Check if the ASCII value of the character is even
#             out=out+i #               Append the character to the output string
# print(out)     #   Print the final output string

# n=input('enter a  string: ')
# out=''
# for i in n:
#     if ord(i)==32:
#         out=out+"*"
#     else:
#         out=out+i
    
# print(out)

