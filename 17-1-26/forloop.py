#Find and print the sum of odd digit and the sum of even digit of the given number

# a=int(input("Enter a number: ")) #  Program to calculate sum of even and odd digits in a number Take input from user and convert to integer
# odd=0 #  Initialize counters for even and odd digits
# even=0
# temp=str(a) #  Convert the number to string to iterate through each digit
# for i in temp: #  Iterate through each digit in the number
#     if (int(i)) %2==0: #  Check if the digit is even
#         even+=int(i) #  Add even digit to even sum
#     else:
#         odd+=int(i) #  Add odd digit to odd sum
# print(even) #  Print the sum of even digits
# print(odd) #  Print the sum of odd digits

#WAP to print the fibonacci series upto n terms
# num=int(input("Enter a number: "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(1,num-1):
#     c=a+b
#     a=b
#     b=c
#     print(c)


#WAP to print  the sum of  fibonacci series upto n terms
# num=int(input("Enter a number: "))
# a=0 #  Initialize first two terms of Fibonacci series
# b=1
# sum=1 #  Initialize sum with the first two terms
# print(a) #  Print the first two terms
# print(b)
# for i in range(1,num-1): #  Generate the remaining terms of Fibonacci series
#     c=a+b #  Calculate the next term in the series
#     a=b #  Update the previous two terms
#     b=c
#     print(c) #  Print the current term
#     sum+=c #  Add the current term to the sum
# print('The sum of above series is : ',sum) #  Print the sum of the series


#WAP to find HCF of the given two numbers
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

# WAP to get the following output
# s=’example on for loop’
# output=’ee on fr lp’
# s='example on for loop'
# output=[]
# final=''
# temp= list(s)
# output.append(temp[0])
# for i in range (len(temp)):
#     if temp[i]==' ':
#         output.append(temp[i-1])
#         output.append(temp[i+1])
        
# output.append(temp[-1])
# final=output[0]
# for i in range(1,len(output)):
#     final+=output[i]
# print(final)




#WAP  to print sum of integer from the hetrogenous list using for loop
# a=eval(input("Enter a list:")) #  Program to calculate the sum of all integers in a user-provided list Get input from user and evaluate it as a list
# sum=0 #  Initialize sum variable to 0
# for i in a: #  Iterate through each element in the list
#     if type(i)==int: #  Check if the current element is of integer type
#         sum+=i #  If it's an integer, add it to the sum
# print(sum) #  Print the final sum of all integers in the list