# Find the largest of three numbers
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# c=int(input('Enter third number: '))
# if a>b and a>c:                 # check if a is largest
#     print(f'{a} is the largest number')
# elif b>a and b>c:                # check if b is largest            
#     print(f'{b} is the largest number')
# elif c>a and c>b:                      # check if c is largest
#     print(f'{c} is the largest number')
# else:
#     print(f'All numbers are equal {a}') # when a==b==c

# #WAP to find smallest among 4 number using elif
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))   
# c=int(input('Enter third number: '))
# d=int(input('Enter fourth number: '))
# if a<b and a<c and a<d:                 # check if a is smallest
#     print(f'{a} is the smallest number')
# elif b<a and b<c and b<d:                # check if b is smallest
#     print(f'{b} is the smallest number')
# elif c<a and c<b and c<d:                      # check if c is smallest
#     print(f'{c} is the smallest number')
# elif d<a and d<b and d<c:                      # check if d is smallest
#     print(f'{d} is the smallest number')
# else:
#     print('Some or all numbers are equal') # when some or all numbers are equal 

# WAP to check whether a number is positive, negative or zero
# num=int(input('Enter a number: '))
# if num>0:          # check if number is positive
#     print(f'{num} is a positive number')
# elif num<0:        # check if number is negative
#     print(f'{num} is a negative number')
# else:              # when number is zero
#     print('The number is zero')

# WAP to check whether a number is divisible by 3 or 5 or both
# num=int(input('Enter a number: '))
# if num%3==0 and num%5==0: # check if divisible by both 3 and 5
#     print('FIZZBUZZ')
# elif num%3==0:          # check if divisible by 3
#     print('FIZZ')   
# elif num%5==0:        # check if divisible by 5
#     print('BUZZ')
# else:
#     print(f'{num} is not divisible by either 3 or 5') 

#WAP to check if a given char is vowel or not using nested if
# ch=input('Enter a character: ')
# if len(ch)==1:                     # check if input is a single character
#     if 'A'<=ch<='Z' or 'a'<=ch<='z':  # check if character is an alphabet
#         if ch in 'aeiouAEIOU':         # check if character is a vowel
#             print(f'{ch} is a vowel')
#         else:                          # when character is not a vowel
#             print(f'{ch} is not a vowel')
#     else:                              # when character is not an alphabet
#         print('Please enter an alphabet character')  # input validation
# else:                              # when input is not a single character
#     print('Please enter a single character')  # input validation


# WAP to validate username and password using nested if
# user='abc'
# passw='123'
# username=input('Enter username: ')
# if username==user:                      # check if username is correct
#     password=input('Enter password: ')
#     if password==passw:                 # check if password is correct
#         print('Login successful')
#     else:                               # when password is incorrect
#         print('Incorrect password')
# else:                                   # when username is incorrect
#     print('Incorrect username')         # input validation

#WAP to find greatest among 3 numbers using nested if 
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# c=int(input('Enter third number: '))
# if a>=b:                            # check if a is greater than or equal to b
#     if a>=c:                        # check if a is greater than or equal to c
#         print(f'{a} is the greatest number')
#     else:                           # when c is greater than a
#         print(f'{c} is the greatest number')
# else:                               # when b is greater than a
#     if b>=c:                        # check if b is greater than or equal to c
#         print(f'{b} is the greatest number')
#     else:                           # when c is greater than b
#         print(f'{c} is the greatest number') 

#WAP to find greatest among 4 numbers using nested if
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# c=int(input('Enter third number: '))
# d=int(input('Enter fourth number: '))
# if a>=b:    # check if a is greater than or equal to b
#     if a>=c:                       # check if a is greater than or equal to c
#         if a>=d:                 # check if a is greater than or equal to d
#             print(f'{a} is the greatest number')
#         else:                    # when d is greater than a
#             print(f'{d} is the greatest number')
#     else:                     # when c is greater than a
#         if c>=d:               # check if c is greater than or equal to d
#             print(f'{c} is the greatest number')
#         else:                 # when d is greater than c
#             print(f'{d} is the greatest number')
# else:                         # when b is greater than a
#     if b>=c:                   # check if b is greater than or equal to c
#         if b>=d:            # check if b is greater than or equal to d
#             print(f'{b} is the greatest number')
#         else:                 # when d is greater than b
#             print(f'{d} is the greatest number')
#     else:                  # when c is greater than b
#         if c>=d:           # check if c is greater than or equal to d
#             print(f'{c} is the greatest number')
#         else:              # when d is greater than c   
#             print(f'{d} is the greatest number')
