#WAP to print the following pattern:-
""" 
A B C D E
  B C D E
    C D E
      D E
        E

 """
n = 5

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(i, n):
        print(chr(65 + k), end="")
    print()
