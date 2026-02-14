#WAP to print pattern:-

"""
R
R a
R a h
R a h u
R a h u l

"""
word=input("Enter a word: ")
n=len(word)
for i in range(1,n+1):
    for j in range(1,i+1):
        print(word[j-1],end=" ")
    print()

