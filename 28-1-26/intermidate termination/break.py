#WAP to guess the number:- 
# while True:
#     n=int(input("enter the number:"))
#     if n>5:
#         print("number is greater than number")
#     elif n<5:
#         print("number is less than number")
#     else:
#         print("you guessed the number🎊🎊🎊")
#         break

#WAP to check the give list is homogenous or not [1,2,3,4,5,6,7,8,9,10]

l=eval(input("enter the list:"))
print(type(l))
for i in range(1,len(l)-1):
    if type(l[i])!=type(l[i+1]):
        print("list is not homogenous")
        break
else:
    print("list is homogenous")












# #WAP to check whether the number is prime or not
# n=int(input("enter the number:"))
# for i in range(2,n):
#     if n%i==0:
#         print("number is not prime")
#         break
# else:
#     print("number is prime")
