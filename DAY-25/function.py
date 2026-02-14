
#&WAP to check whether given number is even or odd

# def evenodd(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")

# a=int(input("enter a number:"))
# evenodd(a)



# a=int(input("enter a number:"))
# if a%2==0:
#     print(a," is even")
# else:
#     print(a,"is odd")

#&Function without args and without return type

# def check():
#     n=int(input("enter a number:"))
#     if n%2==0:
#         print(n,"is even")
#     else:
#         print(n,"is odd")

# check()

#&Function with args and without return type

# WAP to extrct only vowel from given string
# def vowel(s):
#     out=[]
#     for i in s:
#         if i in "aeiouAEIOU":
#             out.append(i)
#     print(out)

# data=input("Enter a string : ") 
# vowel(data)

#  WAP to extract only integers data from hetrogenous list
def extract(s):
    out=[]
    for i in s:
        if type(i)==int:
            out.append(i)
    print(out)
    
a=eval(input("Enter a list to check : "))
extract(a)
