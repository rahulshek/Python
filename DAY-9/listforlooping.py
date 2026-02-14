#WAP to remove duplicates from list 
# a=eval(input("Enter a list:")) # Take input from the user
# out=[] #  Initialize an empty list to store unique elements
# for i in a: #  Iterate through each element in the input list
#     if i not in out: #  Check if the element is not already in the output list
#         out.append(i) #  If not, add it to the output list
# print(out) #  Print the list with unique elements

#WAP to check if a given list is homogenous list or not . A list is homogenous if all the elements in the list are of the same data type
# a=eval(input("Enter a list:"))  # Take input from the user
# check=type(a[0])    #  Determine the type of the first element to compare against
# counter=0 #  Initialize counter to track elements of different types
# for i in a: #  Iterate through each element in the list
#     if type(i)!=check: #  Compare type of current element with the first element's type
#         counter+=1 #  Increment counter if types don't match
# if counter==0: #  If counter is 0, all elements have the same type
#     print("Homogenous") #  Print "Homogenous" if all elements are of the same type
# else: #  Otherwise, elements have different types
#     print("Not Homogenous") #  Print "Not Homogenous" if there are elements of different types

#WAP to count number of time a particular char is repeated in a string using for loop
# a=eval(input("Enter a string:")) # Take input from the user
# chr=eval(input("Enter a character:")) # Take input from the user
# count=0 #  Initialize counter to 0
# for i in a:
#     if i==chr:
#         count+=1
    
# print(chr,"is repeated",count) #  Print the count of the character in the string

#Create a list of cube of numbers between 1 to 30
a=[]
for i in range (1,31):
    a.append(i**3)
print(a)

#Extract all the integers from the list which are multiple of 5 and is three digit number from list
input=[12,34,'lemon',50,200,9+8j,550]
a=[]
for i in input:
    if type(i)==int:
        if i%5==0 and i>99 and i<1000:
            a.append(i)
print(a)

