
# WAP to create a list consist of 1 to 20 integer’s 

# l = [i for i in range(1,21)]
# print(l)

# WAP to create a list consist of 1 to 20 even integer’s
# l = [i for i in range(1,21) if i%2==0]
# print(l)

# WAP to create a list of square between 1 to 20 those are multiple of 3 
# l = [i**2 for i in range(1,21) if i%3==0]
# print(l)

# WAP to store  the square’s of integer’s if integer is even keep square else store cube of the integer from 1 to 20
# l = [i**2 if i%2==0 else i**3 for i in range(1,21)]
# print(l)

#*------------------------------------------------------------------------------------------------

# WAP to extract string from the list only if it is palindrome

# l=['hi',100,3.2,'madam','appa','bye']
# out=[i for i in l if type(i)==str and i==i[::-1]]
# print(out)

#*------------------------------------------------------------------------------------------------

# Get the following output
# s=’programs based open comprehension happy’
# out=[’programs’,’bd’,’open’,’cn’,’hy’]

# s='programs based open comprehension happy'
# out=[i if len(i)%2==0 else i[0]+i[-1] for i in s.split()]
# print(out)

#*------------------------------------------------------------------------------------------------

# Get the following output
# out=[ ( ‘A’ , 1 ) , ( ‘A’ , 2) , ( ‘ A ‘ ,3 ) , ( ‘B’ , 1 ) , ( ‘ B ’ ,2 ) , ( ‘ B’ , 3 ) ]


# out=[(i,j) for i in 'AB' for j in range(1,4)]
# print(out)

#*------------------------------------------------------------------------------------------------

# temp=[0,20,37,100]
# # convert each to farhenheit
# out=[(i*(9/5)+32) for i in temp]
# print(out)  

#*------------------------------------------------------------------------------------------------

students =['Anaya', 'Rohit' , 'Sneha' , 'Aarav' , 'Meera' , 'Karan' , 'Isha' , 'Vivek' , 'Tanya' , 'Rahul']
marks=[85,72,90,67,88,76,95,60,82,78]

# out=[i for i in students if i[0]=='A']
# print(out)

#*------------------------------------------------------------------------------------------------
# Give a list consisting the name followed by the marks of particular student

# out=[(i,j) for i,j in zip(students,marks)]
# print(out)

#*------------------------------------------------------------------------------------------------

# list of of students getting more than average marks 

# out=[i for i,j in zip(students,marks) if j>sum(marks)//len(marks)]
# print(out)

#*------------------------------------------------------------------------------------------------

# Create a list of grades ( "A" , "B" , "C" ) for each
# student based on their marks:
# A → Marks ≥ 85
# B → 70 ≤ Marks < 85
# C → Marks < 70 

gradeA=[i for i,j in zip(students,marks) if j>=85]
gradeB=[i for i,j in zip(students,marks) if j<85 and j>=70]
gradeC=[i for i,j in zip(students,marks) if j<70]
print(gradeA)
print(gradeB)
print(gradeC)