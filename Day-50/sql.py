import random
import sqlite3
from datetime import date


def table_creation():
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()
    # --------------MAIN EMPLOYEE TABLE-----------------
    cursor.execute(
        '''CREATE TABLE EMPLOYEE(ENAME VARCHAR,EMPID NUMBER , DEPARTMENT VARCHAR ,MOBILENUMBER NUMBER ,SALARY NUMBER,JD DATE) ''')
    # --------------SALES DEPARTMENT-----------------
    cursor.execute(
        '''CREATE TABLE SALES(ENAME VARCHAR,EMPID NUMBER , DEPARTMENT VARCHAR ,MOBILENUMBER NUMBER ,SALARY NUMBER,JD DATE,MANAGER VARCHAR) ''')
    # --------------HR DEPARTMENT--------------------
    cursor.execute(
        '''CREATE TABLE HR(ENAME VARCHAR,EMPID NUMBER , DEPARTMENT VARCHAR ,MOBILENUMBER NUMBER ,SALARY NUMBER,JD DATE,MANAGER VARCHAR)''')
    # --------------IT DEPARTMENT--------------------
    cursor.execute(
        '''CREATE TABLE IT(ENAME VARCHAR,EMPID NUMBER , DEPARTMENT VARCHAR ,MOBILENUMBER NUMBER ,SALARY NUMBER,JD DATE,MANAGER VARCHAR) ''')

    data.commit()
    data.close()

# table_creation()


def insert_data(obj):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()
    cursor.execute(f"INSERT INTO EMPLOYEE VALUES(?,?,?,?,?,?)", (obj.ENAME, obj.EMPID, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD))
    if obj.DEPARTMENT == 'Sales':
        cursor.execute(f"INSERT INTO SALES VALUES(?,?,?,?,?,?,?)", (obj.ENAME, obj.EMPID, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD, obj.Manager))
    elif obj.DEPARTMENT == 'HR':
        cursor.execute(f"INSERT INTO HR VALUES(?,?,?,?,?,?,?)", (obj.ENAME, obj.EMPID, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD, obj.Manager))
    elif obj.DEPARTMENT == 'IT':
        cursor.execute(f"INSERT INTO IT VALUES(?,?,?,?,?,?,?)", (obj.ENAME, obj.EMPID, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD, obj.Manager))
    else:
        print('INVALID DEPARTMENT')
    data.commit()
    data.close()


class Bank:
    # Manager = 'Mr Shyam'
    Location = 'Navrangpura'
    Manager = {'Sales': "Mr Rohit", "IT": "Mr Shyam", "HR": "Mr Raj"}

    def __init__(self, ename, department, mobnumber, salary):
        self.ENAME = ename
        self.EMPID = random.randint(1000, 9000)
        self.DEPARTMENT = department
        self.MOBNUMBER = mobnumber
        self.JD = date.today()
        self.SALARY = salary
        self.Manager = Bank.Manager[department]
        insert_data(self)
        print('DATA INSERTED SUCESSFULLY')


s1 = Bank('YASHRAJ', 'IT', 363434266, 250000)
s2 = Bank('KUNAL', 'Sales', 363434266, 250000)
s3 = Bank("Smit", "HR", 900000000, 20000)
