
#& WAP to convet int to binary using loops

""" 
n=5
out=""
while n>=1:
    temp=n%2
    out=str(temp)+out
    n=n//2
print(int(out))
"""

"""

n=int(input("enter a number: ")) 
b=n
out=""
for i in range(n):
    temp=n%2
    out=str(temp)+out
    n=n//2
    if n == 0:
        break
print(out)
print(bin(b))

"""

#& wap to print int from binary

# n=1010
# power=len(str(n))-1
# out=0
# for i in str(n):
#     out=out+(2**power)*int(i)
#     power-=1
# print(out)

#^--------------------------------------------------------------------
#& input="my name is gadha"
#& output="My Name Is Gadha"
# input="my name is gadha"
# out=""
# for i in range(0,len(input)):
#     if i==0:
#         out=out+chr(ord(input[i])-32)
#     elif input[i-1]==" ":
#         out=out+chr(ord(input[i])-32)
#     else:
#         out=out+input[i]
# print(out)







