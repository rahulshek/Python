
#~--------------------------------------------------------------------

# 1. Reverse a String
# Input:  "hello"
# Output: "olleh"

# n="hello"
# out=""
# for i in n:
#     out=i+out
# print(out)

#~--------------------------------------------------------------------

# 2. Check if a Number is Palindrome
# Input:  121
# Output: True

# Input:  123
# Output: False

# n=123
# s=n
# out=0
# while n>0:
#     rem=n%10
#     out=out*10+rem
#     n=n//10
# if out==s:
#     print("True")
# else:
#     print("False")

#~--------------------------------------------------------------------

# 3. FizzBuzz
# Print numbers 1–30.
# Multiples of 3 → "Fizz"
# Multiples of 5 → "Buzz"
# Multiples of both → "FizzBuzz"


# _3=[]
# _5=[]
# _35=[]
# for i in range(1,31):
#     if i%3==0 and i%5==0:
#         _35.append(i)
#     elif i%3==0:
#         _3.append(i)
#     elif i%5==0:
#         _5.append(i)
# print(_3)
# print(_5)
# print(_35)

#~--------------------------------------------------------------------

# 4. Find Duplicates in a List
# Input:  [1, 2, 3, 2, 4, 1, 5]
# Output: [1, 2]

# l=[1, 2, 3, 2, 4, 1, 5]
# out=[]
# for i in l:
#     if l.count(i)>1:
#         if i not in out:
#             out.append(i)
# print(out)
    
#~--------------------------------------------------------------------

# 5. Flatten a Nested List
# Input:  [1, [2, 3], [4, [5, 6]]]
# Output: [1, 2, 3, 4, 5, 6]

# l=[1, [2, 3], [4, [5, 6]]]
# out=[]
# for i in l:
#     if type(i)==list:
#         for j in i:
#             out.append(j)
#     else:
#         out.append(i)
# print(out)

#~--------------------------------------------------------------------

# 6. Anagram Checker
# Input:  "listen", "silent"
# Output: True

# Input:  "hello", "world"
# Output: False

# n="listen", "silent"
# if sorted(n[0]) == sorted(n[1]):
#     print("True")
# else:
#     print("False")

#~----------------------------------------------------------------------

# n=145
# s=n
# out=0
# while n>0:
#     rem=n%10
#     fact =1
#     for i in range (1, rem+1):
#         fact*=i
#     sum+=fact

# if sum == s:
#     print(s," is a Strong Number...")
# else:
#     print(s," is not a Strong Number...")

#~--------------------------------------------------------------------
