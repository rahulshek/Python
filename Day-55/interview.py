
# ~--------------------------------------------------------------------

# 1. Reverse a String
# Input:  "hello"
# Output: "olleh"

# n="hello"
# out=""
# for i in n:
#     out=i+out
# print(out)

# ~--------------------------------------------------------------------

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

# ~--------------------------------------------------------------------

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

# ~--------------------------------------------------------------------

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

# ~--------------------------------------------------------------------

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

# ~--------------------------------------------------------------------

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

# ~----------------------------------------------------------------------

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

# ~--------------------------------------------------------------------

# 7. Find the Largest Prime Number in a List
# Input:  [10, 7, 22, 45, 95, 11]
# Output: 11

# l=eval(input("Enter a list of numbers: "))
# out=[]
# for i in l:
#     for j in range(2,(i//2)+1):
#         if i%j==0:
#             break
#     else:
#         out.append(i)

# final=max(out)
# print(final)

# ~--------------------------------------------------------------------

# 8. Find the Longest Word in a String
# Input:  "The quick brown fox jumps over the lazy dog"
# Output: "jumps"
# l=input("Enter a string: ")
# out=""
# for i in l.split():
#     if len(i)>len(out):
#         out=i
# print(out)

# ~--------------------------------------------------------------------

# 9. Find the Second Largest Number in a List
# Input:  [1, 2, 3, 4, 5]
# Output: 4

# # l=[1, 2, 3, 4, 5]
# l=eval(input("Enter a list of numbers: "))
# largest=max(l)
# l.remove(largest)
# second_largest=max(l)
# print(second_largest)

# ~--------------------------------------------------------------------

# 10. Find the Most Frequent Element in a List
# Input:  [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# Output: 4

# l=[1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
# out=0
# for i in l:
#     if l.count(i)>out:
#         out=l.count(i)
#         final=i
# print(final)

# ~--------------------------------------------------------------------

# 11. Find the Sum of All Even Numbers in a List
# Input:  [1, 2, 3, 4, 5, 6]
# Output: 12

# l=[1, 2, 3, 4, 5, 6]
# out=0
# for i in l:
#     if i%2==0:
#         out+=i
# print(out)

# ~--------------------------------------------------------------------

# 12. Find the Average of All Numbers in a List
# Input:  [1, 2, 3, 4, 5]
# Output: 3
# l=[1, 2, 3, 4, 5]
# out=0
# for i in l:
#     out+=i
# print(out/len(l))

# ~--------------------------------------------------------------------

# 13. Find the Maximum and Minimum Number in a List
# Input:  [1, 2, 3, 4, 5]
# Output: (5, 1)
# l=[1, 2, 3, 4, 5]
# print(max(l), min(l))

# ~--------------------------------------------------------------------

# 14. Find the Number of Vowels in a String
# Input:  "Hello, World!"
# Output: 3
# s="Hello, World!"
# vowels="aeiouAEIOU"
# count=0
# for i in s:
#     if i in vowels:
#         count+=1
# print(count)

# ~--------------------------------------------------------------------

# 15. Find the Number of Words in a String
# Input:  "Hello, World!"
# Output: 2
# s="Hello, World!"
# out=0
# for i in s.split():
#     out+=1
# print(out)

# ~--------------------------------------------------------------------

# 16. Find the Number of Characters in a String
# Input:  "Hello, World!"
# Output: 13
# s="Hello, World!"
# print(len(s))

# ~--------------------------------------------------------------------

# class A:
#     def spam(self):
#         print("Spam method in class A")


# class B():
#     def spam(self):
#         print("Spam method in class B")

# class C(A, B):
#     pass

# c=C()
# c.spam()

# ~--------------------------------------------------------------------

# 17. Find the Number of Occurrences of a Character in a String
# Input:  "Hello, World!", "o"
# Output: 2
# s="Hello, World!"
# char="o"
# count=0
# for i in s:
#     if i==char:
#         count+=1
# print(count)

# ~--------------------------------------------------------------------

# 18. Find the Number of Occurrences of a Word in a String
# Input:  "Hello, World!", "World"
# Output: 1
# s="Hello, World!" ,"World"
# word="World"
# count=0
# for i in s.split():
#     if i==word:
#         count+=1
# print(count)

# ~---------------------------------------------------------------------------------------------------

n = 153
s = n
pow = len(str(n))
sum = 0
while n > 0:
    rem = n % 10
    sum = sum+rem**pow
    n = n//10

if s == sum:
    print("Armstrong")
else :
    print("Not armstrong")

#~-----------------------------------------------------------------------------

n=145
s=n
sum=0
while n>0:
    rem=n%10
    fact=1
    for i in range (1 , rem+1):
        fact*=i
    sum+=fact
    n=n//10
print(sum)

