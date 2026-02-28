
# def demo():
#     c=20
#     d=40
#     def demo2():
#         nonlocal c
#         c+=12
#         print(c,d)
#     demo2()
#     print(c,d)
# demo()


# WAP to  print factorial of a given number 

n=int(input("Enter a number : "))
temp=n
out=1
while n>0:
    out*=n
    n=n-1

print("Fact of " ,temp, " is : " , out)


# WAP a program to extract only vowel from the string

a=input("Enter a string : ")
out=""
s=len(a)-1
while s>0:
    if a[s] in "aeiouAEIO":
        out=a[s]+out
    s=s-1

print(out)





# WAP to print  Fibonacci serries up to n

n=int(input("Enter a number till you want serires : "))  # 0 1 1 2 3
first=0
second=1
print(first)
print(second)
while n-2>0:
    c=first+second
    print(c)
    first=second
    second=c
    n=n-1
    
    
