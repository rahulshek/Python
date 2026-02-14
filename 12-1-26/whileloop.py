# Factorial of a number using while loop
""" 
num=int(input("Enter a number: "))  #input from user
sum=1                               #initializing sum variable
i=1                                #initializing counter variable
while i<=num:                      #looping from 1 to num
    sum=sum*i                      #calculating factorial
    i=i+1                   #incrementing counter
print(sum)             #printing factorial

 """

#WAP to  to get  the following output
# c=’PuTH@1!2
# output:-
# upper=[’P’,’T’,’H’]
# lower=[’y’]
# digit=[’1’,’2’]

# special=[’!’]
""" 
c='PuTH@1!2'          
upper=[]                         # To store uppercase letters
lower=[]                         # To store lowercase letters
digit=[]                         # To store digits
special=[]                       # To store special characters
i=0                              # Initializing counter variable
while i<len(c):                  # Looping through each character in the string
    if 'A'<=c[i]<='Z':           # Checking for uppercase letters
        upper.append(c[i])
    elif 'a'<=c[i]<='z':         # Checking for lowercase letters
        lower.append(c[i])
    elif '0'<=c[i]<='9':         # Checking for digits
        digit.append(c[i])
    else:                        # If not upper, lower or digit, it's a special character
        special.append(c[i])
    i=i+1
print("upper=",upper)
print("lower=",lower)
print("digit=",digit)
print("special=",special)

 """
 
# c='PuTH@1!2'          
# upper=0                         # To store uppercase letters
# lower=0                         # To store lowercase letters
# digit=0                         # To store digits
# special=0                       # To store special characters
# i=0                              # Initializing counter variable
# while i<len(c):                  # Looping through each character in the string
#     if 'A'<=c[i]<='Z':           # Checking for uppercase letters
#         upper=upper+1
#     elif 'a'<=c[i]<='z':         # Checking for lowercase letters
#         lower=lower+1
#     elif '0'<=c[i]<='9':         # Checking for digits
#         digit=digit+1
#     else:                        # If not upper, lower or digit, it's a special character
#         special=special+1
#     i=i+1
# print("upper=",upper)
# print("lower=",lower)
# print("digit=",digit)
# print("special=",special)

#WAP to print in the following format:- uPTH12@!
# c='PuTH@1!2'
# upper=''                         # To store uppercase letters
# lower=''                         # To store lowercase letters
# digit=''                         # To store digits
# special=''                       # To store special characters
# i=0                              # Initializing counter variable
# while i<len(c):                  # Looping through each character in the string
#     if 'A'<=c[i]<='Z':           # Checking for uppercase letters
#         upper=upper+c[i]
#     elif 'a'<=c[i]<='z':         # Checking for lowercase letters
#         lower=lower+c[i]
#     elif '0'<=c[i]<='9':         # Checking for digits
#         digit=digit+c[i]
#     else:                        # If not upper, lower or digit, it's a special character
#         special=special+c[i]
#     i=i+1
# print(lower+upper+digit+special)

 
