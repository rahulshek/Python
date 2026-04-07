
# import math
# # ^-------------------------------------Simple Calculator--------------------------------------------

# # *---------------------------------Add Logic -------------------------------------------------------


# def add(a1, a2):
#     return a1+a2


# # #*----------------------------- Sub Logic --------------------------------------------------------------

# def sub(a, b):
#     if a > b:
#         print(a-b)
#     else:
#         print("-ve sum can't be possible.")


# # *---------------------------------Multiplication Logic ------------------------------------------------------

# def multi(a, b):
#     return a*b

# # *---------------------------------Div Logic ------------------------------------------------------------


# def div(a, b):
#     return a/b

# # *-----------------------------------Power Logic -------------------------------------------------------------


# def pow(a, b):
#     return a**b

# # *----------------------------------- Square Root Logic -------------------------------------------------------------


# def sqrt(a):
#     return math.sqrt(a)

# # *-----------------------------------Cube Root Logic -------------------------------------------------------------


# def cube(a):
#     return a**(1/3)

# # *-----------------------------------Factorial Logic -------------------------------------------------------------


# def fact(a):
#     if a == 0 or a == 1:
#         return 1
#     else:
#         return a*fact(a-1)

# # ~-----------------------------------------------Main Logic -----------------------------------------------------


# s = True
# while s == True:
#     print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Power \n6. Square Root \n7. Cube Root \n8. Factorial")
#     ch = int(input("Enter your choice: "))
#     if ch == 1:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         print(add(num1, num2))
#     elif ch == 2:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         sub(num1, num2)
#     elif ch == 3:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         print(multi(num1, num2))
#     elif ch == 4:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         print(div(num1, num2))
#     elif ch == 5:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         print(pow(num1, num2))
#     elif ch == 6:
#         num1 = int(input("Enter the number: "))
#         print(sqrt(num1))
#     elif ch == 7:
#         num1 = int(input("Enter the number: "))
#         print(cube(num1))
#     elif ch == 8:
#         num1 = int(input("Enter the number: "))
#         print(fact(num1))
#     else:
#         print("Invalid Choice")
#     s = input("Do you want to continue? (y/n): ")
#     if s == "y":
#         s = True
#     else:
#         s = False
#         print("Sign off successfully.......")


# def pack(*args):
#     return args


# print(pack(1, 2, 3, 4, 5))


# def pakeep(**kwargs):
#     return kwargs


# print(pakeep(mao="John", name="python", version=3.9, type="programming language"))

inp=["eat","tea","tan","ate","nat","bat"]
# out=[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
out={}

for i in inp:
    key="".join(sorted(i))
    if key not in out:
        out[key]=[]
    out[key].append(i)
print(out.values())


