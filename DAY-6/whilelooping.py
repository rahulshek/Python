#WAP to reverse a string using while loop
""" 
ch=input("Enter a string: ")
output=""                #to store reversed string
i=0
while i<len(ch):         # Iterate through each character in the string
    output=ch[i]+output  # Prepend current character to output
    i+=1                 # Move to the next character
print(output)
 """

#WAP to check if a given string is palindrome or not using while loop 
""" 
ch=input("Enter a string: ")
output=""                #to store reversed string
i=0
while i<len(ch):         # Iterate through each character in the string
    output=ch[i]+output  # Prepend current character to output
    i+=1                 # Move to the next character
if ch==output:           # Compare original string with reversed string
    print("Palindrome and string is :",output)
else:                    # If strings are not equal, it's not a palindrome
    print("Not a Palindrome") 
"""


#WAP to reverse the number using while loop
""" 
num=int(input("Enter a number: "))
output=0                             #to store reversed number
while num>0:
    ld=num%10                        #get last digit
    output=output*10+ld              #append last digit to output
    num=num//10                      #remove last digit from number
print("Reversed number is :",output) #print the reversed number
 """


#WAP to check if a given number is palindrome or not using while loop
""" 
org=num=int(input("Enter a number: "))
output=0                                         #to store reversed number
while num>0:
    ld=num%10                                    #get last digit
    output=output*10+ld                          #append last digit to output
    num=num//10  
if org==output:                                  # Compare original number with reversed number
    print("Palindrome and number is :",output)
else:
    print("Not a Palindrome")                    #remove last digit from number

 """

#WAP to check if a given number is prefect number or not using while loop
""" 
num=int(input("Enter a number:"))
i=1                         #to iterate from 1 to num-1
sum=0                       #to store sum of factors
while i<num:
    if num%i==0:            #check if i is a factor of num
         sum=sum+i          #add factor to sum
    i+=1                    #increment i
if sum==num:                #check if sum of factors equals num
    print("Perfect number")
else:
    print("Not a Perfect number")
  """