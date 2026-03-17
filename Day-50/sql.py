import sqlite3
from datetime import date


def table_creation():
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    # * --------------MAIN EMPLOYEE TABLE-----------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS EMPLOYEE(EMPID INTEGER PRIMARY KEY AUTOINCREMENT , ENAME TEXT, DEPARTMENT TEXT, MOBILENUMBER BIGINT, SALARY INTEGER, JD TEXT)
    ''')

    # * --------------SALES DEPARTMENT-----------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SALES( EMPID INTEGER, ENAME TEXT, DEPARTMENT TEXT, MOBILENUMBER BIGINT, SALARY INTEGER, JD TEXT,MANAGER TEXT)
    ''')

    # * --------------HR DEPARTMENT--------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HR( EMPID INTEGER, ENAME TEXT, DEPARTMENT TEXT, MOBILENUMBER BIGINT, SALARY INTEGER, JD TEXT, MANAGER TEXT)
    ''')

    # * --------------IT DEPARTMENT--------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS IT( EMPID INTEGER, ENAME TEXT, DEPARTMENT TEXT, MOBILENUMBER BIGINT, SALARY INTEGER, JD TEXT, MANAGER TEXT)
    ''')

    data.commit()
    data.close()


table_creation()


# * -------------------Insert Data-----------------

def insert_data(obj):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute(
        "INSERT INTO EMPLOYEE(ENAME,DEPARTMENT,MOBILENUMBER,SALARY,JD) VALUES(?,?,?,?,?)",
        (obj.ENAME, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD)
    )

    obj.EMPID = cursor.lastrowid

    if obj.DEPARTMENT == 'Sales':
        cursor.execute("INSERT INTO SALES VALUES(?,?,?,?,?,?,?)",
                       (obj.EMPID, obj.ENAME, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD, obj.Manager))

    elif obj.DEPARTMENT == 'HR':
        cursor.execute("INSERT INTO HR VALUES(?,?,?,?,?,?,?)",
                       (obj.EMPID, obj.ENAME, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD, obj.Manager))

    elif obj.DEPARTMENT == 'IT':
        cursor.execute("INSERT INTO IT VALUES(?,?,?,?,?,?,?)",
                       (obj.EMPID, obj.ENAME, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD, obj.Manager))

    else:
        print('INVALID DEPARTMENT')

    data.commit()
    search_employee(obj.EMPID)
    data.close()


# * -------------------Display Data-----------------

def display_all():
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute("SELECT * FROM EMPLOYEE")
    records = cursor.fetchall()

    for i in records:
        print(i)

    data.close()


# * -------------------Search Employee-----------------

def search_employee(empid):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute("SELECT * FROM EMPLOYEE WHERE EMPID=?", (empid,))
    record = cursor.fetchone()

    if record:
        print(record)
    else:
        print("Employee Not Found")

    data.close()


# * -------------------Update Salary-----------------

def update_salary(empid, new_salary):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute("UPDATE EMPLOYEE SET SALARY=? WHERE EMPID=?",
                   (new_salary, empid))

    data.commit()
    data.close()

    print("Salary Updated Successfully")


# * -------------------Delete Employee-----------------

def delete_employee(empid):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute("DELETE FROM EMPLOYEE WHERE EMPID=?", (empid,))

    data.commit()
    data.close()

    print("Employee Deleted Successfully")


# * -------------------Department Employees-----------------

def department_employee(dept):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute(f"SELECT * FROM {dept}")
    records = cursor.fetchall()

    for i in records:
        print(i)

    data.close()

# * -------------------Department Employees-----------------


def department_employee(dept):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute(f"SELECT * FROM {dept}")
    records = cursor.fetchall()

    for i in records:
        print(i)

    data.close()

# *--------------------Login-----------------


def login():
    pass
# * -------------------Class-----------------


class Bank:

    Location = 'Navrangpura'
    Manager = {'Sales': "Mr Rohit", "IT": "Mr Shyam", "HR": "Mr Raj"}

    def __init__(self, ename, department, mobnumber, salary):

        self.ENAME = ename
        self.DEPARTMENT = department
        self.MOBNUMBER = mobnumber
        self.JD = date.today().isoformat()
        self.SALARY = salary
        self.Manager = Bank.Manager[department]

        insert_data(self)

        print('DATA INSERTED SUCCESSFULLY')


# * -------------------Menu-----------------

while True:
    print("""
    1 Add Employee
    2 Display Employees
    3 Search Employee
    4 Update Salary
    5 Delete Employee
    6 Department Employees
    7 Exit
    """)

    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        mob = int(input("Enter Mobile: "))
        sal = int(input("Enter Salary: "))
        Bank(name, dept, mob, sal)

    elif choice == 2:
        display_all()

    elif choice == 3:
        empid = int(input("Enter EMPID: "))
        search_employee(empid)

    elif choice == 4:
        empid = int(input("Enter EMPID: "))
        sal = int(input("Enter New Salary: "))
        update_salary(empid, sal)

    elif choice == 5:
        empid = int(input("Enter EMPID: "))
        delete_employee(empid)

    elif choice == 6:
        dept = input("Enter Department: ")
        department_employee(dept)

    elif choice == 7:
        print("Exiting...")
        break
