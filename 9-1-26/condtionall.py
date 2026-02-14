# Conditional statements in Python

#WAP to print the print the middle char of the given string only if  it is a upparcase char
# ch=input("Enter a string: ")
# length=len(ch)              #Get the length of the string
# if length%2==0:             #Check if length is even
#     print("String length is even, no middle character.")
# else:
#     mid_val=length//2      #Calculate middle index for odd length string using floor division
#     mid_char=ch[mid_val]    #Get the middle character
#     if 'A'<=mid_char<='Z':  #Check if middle character is uppercase
#         print("Middle character is uppercase: '", mid_char, "'")
#     else:                   #If not uppercase
#         print("Middle character is not uppercase.")


#WAP to print reversed string only if the string is starting with vowel and ending with conconets and having middle value

ch=input("Enter a string: ")
length=len(ch)                                     #Get the length of the string
vowels="AEIOUaeiou"                                #Define vowels
if length%2!=0:                                    #Check if length is odd
    if ch[0] in vowels and ch[-1] not in vowels:   #Check if first char is vowel and last char is consonant
        print("Reversed string:", ch[::-1])        #Print reversed string
    else:                                          #If conditions not met
        print("String does not start with a vowel and end with a consonant.")
else:                                              #If length is even
    print("String length is even, no middle character.")