import csv

# with open("data1.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "SID", "Marks"])  # header row
#     writer.writerows([
#         ["Rahul", "1", "40"],
#         ["Mohit", "2", "55"],
#         ["Preskha", "3", "88"]
#     ])

def add_student(name, sid, marks):
    with open("data1.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, sid, marks])
        print("Student added successfully")

# add_student("Meet", "4", "60")
# add_student("Smit","5","10")

def marks_greater_than(marks):
    with open("data1.csv", "r") as file:
        reader =list( csv.reader(file))
        data=reader[1::]  
        for row in data:
            if int(row[2]) > marks:   
                print(row)
#WAP to serch from the recod data2.csv file for the details of the student whose marks are greater than 50'
# with open("data1.csv", "r") as file:
#     reader =list( csv.reader(file))
#     data=reader[1::]  
#     for row in data:
#         if int(row[2]) > 50:   
#             print(row)

n=int(input("Enter the mark greater than which you want to search: "))
marks_greater_than(n)

#*--------------------------------------------------------------------------------------

#