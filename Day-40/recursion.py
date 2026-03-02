

# def factorial(n,fact=1):
#     if n<=0:
#         return fact
#     return factorial(n-1,fact*n)

# print(factorial(5))


#?WAP to extract the vowels from a string using recursion

# a=input("Enter a string : ")
# out=""
# s=len(a)-1
# while s>0:
#     if a[s] in "aeiouAEIO":
#         out=a[s]+out
#     s=s-1

# print(out)


def extraxt(a,out=""):
    s=len(a)-1
    if s<=0:
        return out
    if a[s] in "aeiouAEIO":
        out=a[s]+out
    
    return extraxt(a[:-1], out)


print(extraxt('Hello World'))
    
    

# def extraxt(a,out=""):
#     if len(a)==0:
#         return out
#     if a[-1] in "aeiouAEIO":
#         out=a[-1]+out
#     return extraxt(a[:-1],out)

# print(extraxt("Hello"))