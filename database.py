
import sqlite3

conn=sqlite3.connect("database.db")
cur=conn.cursor()

#cur.execute("CREATE TABLE EXAM (subject char ,subcode varchar ,exam_date  date ,reg_no longint,stname char )")   

#cur.execute("CREATE TABLE students (name char NOT NULL,address varchar NOT NULL,regno  char NOT NULL,mobileno longint NOT NULL,emailid varchar NOT NULL,password varchar NOT NULL)") 
#cur.execute("Delete from students")
#cur.execute("Delete from exam")

#print("Table created")
#cur.execute("ALTER TABLE STUDENT  ADD  COLUMN emailid varchar ")
#cur.execute("DELETE FROM students where name = \"Priya\" ") 
cur.execute("DELETE FROM students")
cur.execute("DELETE FROM exam")
print("row deleted")

#cur.execute("SELECT * from student")
conn.commit()
conn.close()



