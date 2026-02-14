# n=input("Enter a character: ")
# if ord(n)>=65 and ord(n)<=90: #Checking for uppercase letters using ASCII values
#     print("Uppercase Letter")
#     print("ASCII Value:", ord(n))

# n=input("Enter a character: ")
# if 'A'<=n<='Z':  #Alternative way to check for uppercase letters
#     print("Uppercase Letter")
#     print("ASCII Value:", ord(n))

# n=eval(input("Enter a data : ")) #Using eval to take input of any data type
# if type(n) in[list,tuple,set,dict]: #Checking if the input is a collection type
#     print("True") #Printing True if it is a collection type

# write a program to check whether a number is even or odd
# a=int(input("Enter a number: "))
# if a%2==0: #Checking if the number is even
#     print("Even Number")#Printing Even Number if the number is even
# else:
#     print("Odd Number") #Printing Odd Number if the number is not even

#write a program to check palindrome or not 
# s=str(input("Enter a string:"))
# if s==s[::-1]: #Checking if the string is equal to its reverse
#     print("Palindrome") #Printing Palindrome if the condition is true
# else:
#     print("Not a Palindrome") #Printing Not a Palindrome if the condition is false


#WAP to check whether a character is vowel or consonant
# ch=input("Enter a character: ")
# if ch in ['a','e','i','o','u','A','E','I','O','U']: #Checking if the character is in the list of vowels
#     print("Vowel") #Printing Vowel if the condition is true
# else:
#     print("Consonant") #Printing Consonant if the condition is false
# if ch in 'aeiouAEIOU': #Alternative way to check for vowels using string
#     print("Vowel") #Printing Vowel if the condition is true
# else:
#     print("Consonant") #Printing Consonant if the condition is false

#WAp to check whether data is single value data type or collection data type
# data=eval(input("Enter a data: "))
# if type(data) in (int,float,complex,bool): #Checking if the data type is a single value data type
#     print("Single Value Data Type") #Printing Single Value Data Type if the condition is true
# else:
#     print("Collection Data Type") #Printing Collection Data Type if the condition is false

#WAP to check whether a number is single digit, two digit, three digit or more than three digit
# a=int(input("Enter a number: ")) #Taking input of a number
# if a<10:                         #Checking if the number is less than 10
#     print("Single Digit Number") #Printing Single Digit Number if the number is less than 10
# elif a<100:                      #Checking if the number is less than 100
#     print("Two Digit Number") #Printing Two Digit Number if the number is less than 100
# elif a<1000:                    #Checking if the number is less than 1000
#     print("Three Digit Number") #Printing Three Digit Number if the number is less than 1000
# else:                           #If the number is greater than or equal to 1000
#     print("More than Three Digit Number") #Printing More than Three Digit Number if the number is greater than or equal to 1000


#WAP to check if a given char is upper case or lower case or digit or special char 
# data=input("Enter a data : ")
# if data >='A' and data <='Z': #Checking if the character is an uppercase letter
#     print("Uppercase Letter") #Printing Uppercase Letter if the condition is true
# elif data >='a' and data <='z': #Checking if the character is a lowercase letter
#     print("Lowercase Letter") #Printing Lowercase Letter if the condition is true
# elif data >='0' and data <='9': #Checking if the character is a digit
#     print("Digit") #Printing Digit if the condition is true
# else:                           #If the character is not an uppercase letter, lowercase letter or digit
#     print("Special Character") #Printing Special Character if the condition is false
