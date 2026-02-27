
#&Wap to covert int into binary 

a=int(input("Enter a number : "))
# a=10
out="" 
while a>0:
    out+=str(a%2)
    a=a//2
print(out[::-1])

#&WAP to cnvert binary into int

b=int(input("Enter a binary number :"))
# b=1000
out=0

for i in range(0,len(str(b))):
    out=out+b%10*(2**i)
    b=b//10
print(out)

# b=int(input("Enter a binary number :"))
# i=0
# while b>0:
#     out=out+b%10*(2**i)
#     b=b//10
#     i+=1
# print(out)


