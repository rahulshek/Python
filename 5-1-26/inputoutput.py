# Input and Output in Python

# a=10
# b=20
# print(a)  # Output the value of a
# print(a,b)  # Output the values of a and b using separator as space and end as newline
# print(a,b,sep='-',end=' END\n')  # Output with custom separator and end
# print(a+b)  # Output the sum of a and b 
# a=input("Enter a value: ")   # Take input from user and store in a
# b=input("Enter another value: ")  # Take input from user and store in b
# print(a+b)  # Output the concatenation of a and b as strings    
# print(int(a)+int(b))  # Convert a and b to integers and output their sum
# a=int(input("Enter a value: "))  # Take input, convert to integer and store in a
# b=int(input("Enter another value: "))  # Take input, convert to integer and store in b
# print(a+b)  # Output the sum of a and b as integers

# # Demonstration of various arithmetic operations
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print("Sum:",a+b) # Output the sum of a and b
# print("Difference:",a-b)  # Output the difference of a and b  
# print("Product:",a*b) # Output the product of a and b
# print("Quotient:",a/b) # Output the quotient of a and b
# print("Integer Division:",a//b) # Output the integer division of a and b
# print("Remainder:",a%b) # Output the remainder of a divided by b
# print("Exponentiation:",a**b) # Output a raised to the power of b
# a=int(input("Enter first number: "))
# print(a,type(a))  # Output the value of a and its type
a=eval(input("Enter a value: "))
print(a,type(a))  # Output the value of a and its type after evaluation