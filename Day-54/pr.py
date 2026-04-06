# wap to capitalize only the first letter of every word in the given list
l=["vaidegi","rahul","shivam","kapil","patil"]
l1=[i.capitalize() for i in l]
print(l1)

#*----------------------------------------------------------------------------------

# 4.wap to extract only individual data types form the list

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
str1=[i for i in l if type(i)==str]
int1=[i for i in l if type(i)==int]
float1=[i for i in l if type(i)==float]
complex1=[i for i in l if type(i)==complex]
list1=[i for i in l if type(i)==list]
bool1=[i for i in l if type(i)==bool]
print(str1)
print(int1)
print(float1)
print(complex1)
print(list1)
print(bool1)

#*----------------------------------------------------------------------------------


# 5.wap to extract only individual data types from the list and sum all the individual data types

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
int1=0
str1=""
float1=0.0
list1=[]
bool1=False
for i in l:
    if type(i)==int:
        int1+=i
    elif type(i)==float:
        float1+=i
    elif type(i)==str:
        str1+=i
    elif type(i)==list:
        list1.extend(i)
    elif type(i)==bool:
        bool1|=i
print(int1)
print(float1)
print(str1)
print(list1)
print(bool1)

#*----------------------------------------------------------------------------------

# 6.wap to print the count of alphabets and numbers and space in the given string

s="india got the independence in the year 1947"
alpha=0
num=0
space=0
for i in s:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        num+=1
    elif i.isspace():
        space+=1
print("alphabets:",alpha)
print("numbers:",num)
print("space:",space)

#*----------------------------------------------------------------------------------

# 7.wap to check how many words are present in the given sentence

s="hello world sentence"
count=len(s.split())
print(count)

#*-------------------------------------------------------------------------------

# 8.wap to create a dictionary and print the characters 
# and its Ascii value pair
# s="hello world"
# output:--> {"h":ascii value,"e":ascii value........}

s="hello world"
l={i:ord(i) for i in s}
print(l)

#*----------------------------------------------------------------------------------

# 9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it

# names=["apple","google","yahoo","microsoft","gmail","walmart"]

# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}

names=["apple","google","yahoo","microsoft","gmail","walmart"]
d={i: i if len(i)%2==0 else i[::-1] for i in names}
print(d)

#*----------------------------------------------------------------------------------

# 10.wap to print series of factorial(take user input)

n=int(input("Enter the number"))
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    print(f"{i}!={fact}")

#*----------------------------------------------------------------------------------

# 11.wap to create a dictionary with element and its count pair

# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# output:-->
# {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}

l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
out={}
for i in l:
    if i not in out:
        out[i]=1
    else:
        out[i]+=1
print(out)

#*----------------------------------------------------------------------------------

# 12.wap to find the length of the string without using inbuilt function
s="Never Give Up"
count=0
for i in s:
    count+=1
print(count)

#*----------------------------------------------------------------------------------

# 13.wap to reverse a string without using inbuilt function
x="you did it guys"

out=""
for i in x:
    out=i+out
print(out)

#*------------------------------------------------------------------------------------

# 14.wap to print alternative character from a given string
# s="hello python"

s="hello python"
out=""
for i in range(0,len(s),2):
    out+=s[i]
print(out)


#*-------------------------------------------------------------------------------------


# for loop level 2 questions
# **********************************


# 15.wap to create a dictionary index and word pair
# s="tomorrow is weekend and non-veg special"



# o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}

s="tomorrow is weekend and non-veg special"
out={i: s.split()[i] for i in range(len(s.split()))}
print(out)

#*--------------------------------------------------------------------------------------


# 16.wap to create a dictionary words and its length pair
# s="tomorrow is weekend and non-veg special"


# o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}
s="tomorrow is weekend and non-veg special"
out={i:len(i) for i in s.split()}
print(out)

#*----------------------------------------------------------------------------------------

# 17.wap to create a dictionary characters and its corresponding upper case characters
# s="sunday"


# o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}

s="sunday"
out={i:i.upper() for i in s}
print(out)

#*----------------------------------------------------------------------------------------

# 18.wap to create a dictionary Ascii and character pair
# l=[89,51,111,77,108,120]


# o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}

l=[89,51,111,77,108,120]
out={i:chr(i) for i in l}
print(out)

#*------------------------------------------------------------------------------------------

# 19.wap to  create a list of characters and its Ascii value pair


# s="sunday"


# o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)


s="sunday"
# out=[]
# for i in s:
#     s=(i,ord(i))
#     out.append(s)
# print(out)

out=[(i,ord(i)) for i in s]
print(out)

#*-----------------------------------------------------------------------------------------

# 22.wap to create a dictionary with letter and its words starting with that letter pair


# s="hi hello good morning welcome to python session"


# o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}

s="hi hello good morning welcome to python session"
out={}
for i in s.split():
    # print(i[0])
    if i[0] not in out:
        out[i[0]]=[i]
    else:
        out[i[0]].append(i)
print(out)


#*--------------------------------------------------------------------------------------------------------------------

# 23.wap to create a dictionary of characters and its indices pair
# s="hello python"


# o/p:-->{"h":[0,9],"e":1..........}

s = "hello python"
out = {}

for index, char in enumerate(s):
    if char not in out:
        out[char] = [index]
    else:
        out[char].append(index)

print(out)

#*-------------------------------------------------------------------------------------------------------------------------

# 24.wap to create a dictionary word and reverse word pair
# s="tomorrow is weekend and non-veg special"


# o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}

s="tomorrow is weekend and non-veg special"
out={i:i[::-1] for i in s.split()}
print(out)

#*----------------------------------------------------------------------------------------------------------------------------------
# 25. wap to iterate inside the list check if it is having nested list if yes merge it

# list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]

# #excepted output:-->list1=["hello",10,20.55,True,False,"hai","bye",False,"goodnight","enjoy the holiday"]

list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]
list2=[]
for i in list1:
    if type(i)!=list:
        list2.append(i)
    elif type(i)==list:
        for j in i:
            list2.append(j)
print(list2)

#*--------------------------------------------------------------------------------------------------------------

# 26.wap if a names ends with vowels then reverse a names else print its length
names=["Kumar","Lakita","Umesh a","Priyanka"]

out={}
for i in names:
    if i[-1] in "aeiouAEIOU":
        out[i]=i[::-1]
    else:
        out[i]=len(i)

# var = { key : value if condition else value 2 for var in collection  }
print(out)

#*----------------------------------------------------------------------------------------------------------------

