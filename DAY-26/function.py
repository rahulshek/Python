
#&Function without args and with return values

#?WAp a function that takes a string as an argument and returns a list of all the vowels in the string.

# def extract(n):
#     out=[]
#     for i in n:
#         if i in "aeiouAEIOU":
#             out.append(i)

#     return out

# s=input("Enter a string: ")
# print(extract(s),s)


# def loop(n):
#     for i in range(1,n+1):
#         if i==1:
#             print(i)
#             return"hii"

# print(loop(5))

#create a functionn to extract only the int which are divisible by 5  or 3 form the list 

def extract(n):
    out=[]
    for i in n:
        if type(i)==int:
            if i%3==0 or i%5==0:
                out.append(i)
    return out

# l=["hii",15,24,True,8+9j,7]
l=eval(input("Enter a list :"))
print(extract(l))