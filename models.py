import sqlite3 as sql


def insertstu (sname,address,regno,mobileno,emailid,password):
    conn=sql.connect("database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO STUDENTS (name,address,regno,mobileno,emailid,password) values(?,?,?,?,?,?)" ,(sname,address,regno,mobileno,emailid,password))
    conn.commit()
    conn.close()


def retrivestu ():
    conn=sql.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM students")
    stu=cur.fetchall()
    conn.close()
    return stu


def insertexamreg (subject,subcode,exam_date,reg_no,stname):
    conn=sql.connect("database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO EXAM  (subject,subcode,exam_date,reg_no,stname) values(?,?,?,?,?)" ,(subject,subcode,exam_date,reg_no,stname))
    conn.commit()
    conn.close() 


def retriveex (reg_no):
    conn=sql.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM EXAM where reg_no=reg_no")
    stu=cur.fetchall()
    conn.close()
    return stu