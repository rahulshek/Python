
# *--------------------------------------Exception handling---------------------------------
# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     print(a//b)
# except ValueError:
#     print("Please enter a valid number")
# except ZeroDivisionError:
#     print("Please enter a non-zero number")

# *-------------------------Generic exception handling------------------------------------------

# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     print(a//b)
# except Exception as e:
#     print(e)
#     print("Please enter a valid number")

# *------------------------Default exception handling ---------------------------------------------

# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     print(a//b)
# except Exception as e:
#     print(e)
#     print("Please enter a valid number")

# except KeyboardInterrupt:
#     print("Keyboard Interrupted🤌")


# *-----------------------------Customize exception handling--------------------------------------------

# class CUSTOMISED(Exception):
#     print("You are trying to divide by zero")


# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# if b == 0:
#     raise CUSTOMISED
# else:
#     print(a//b)

#*------------------------------------------------------------------------------------

class CUSTOMISED(Exception):
    def __init__(self, message="🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬"):
        super().__init__(message)
        # print("You are trying to divide by zero")
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if b == 0:
    raise CUSTOMISED
else:
    print(a // b)


# *------------------------------------------------------------------------------------
