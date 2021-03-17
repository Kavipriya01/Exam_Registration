from flask import Flask ,render_template,url_for,request
import sqlite3 as sql
import models as dbHandler
app = Flask( __name__ )
@app.route('/')
@app.route('/home')
@app.route('/home1')
@app.route('/home2')
def home():
    return render_template('home.html')

@app.route('/user_login.html')
@app.route('/loginpg')
@app.route('/userlogin')
def login():
    return render_template('user_login.html')
           
@app.route('/adlogin.html')
def adlogin():
    return render_template('adlogin.html')

@app.route('/examregform')
def  examregform():
    return render_template('examreg.html')   

@app.route('/goadminhome')
@app.route('/gotoadminhome')
def goadminhome():
    return render_template('adhome.html')

@app.route('/adhome',methods=['POST' , 'GET'])    
def adhome():
    if request.method=='GET':
        return  render_template('adhome.html')

@app.route('/register')
def register():
        return render_template('user_reg.html')

@app.route('/gouserhome')
@app.route('/gotouserhome')
@app.route('/gouserhome1')
def gouserhome():
    return render_template('userhome1.html')
@app.route('/userhome',methods=['POST' , 'GET'])    
def userhome():
    if request.method=='GET':
        return  render_template('userhome1.html')       

@app.route('/studetails', methods=['POST','GET'])
def studetails():
    msg="msgin"
    if request.method == 'POST'  :
            sname=request.form['sname']
            address=request.form['address']
            regno=request.form['regno']
            mobileno=request.form['mobileno']
            emailid=request.form['emailid']
            password=request.form['password']
            dbHandler.insertstu(sname,address,regno,mobileno,emailid,password)
            stud=dbHandler.retrivestu()
            msg="RECORDS ADDED SUCCESSFULLY"
            con=sql.connect("database.db")
            con.row_factory=sql.Row

            cur=con.cursor()
            cur.execute('select * from students where regno=?',(regno,))
            rows=cur.fetchall()
            return render_template('confirmpg2.html',msg=msg,rows=rows)


            #@with sql.connect("database.db") as con:
             #       cur=con.cursor()
                    
                    #cur.exeute("INSERT INTO STUDENT0 (name,address,age,mobileno,password) values(?,?,?,?,?)" ,(uname,uaddress,uage,umobileno,upassword) )
              #      con.commit()
               #     msg="RECORDS ADDED SUCCESSFULLY
    else:        
            msg="RECORDS CANNOT BE EXEUTED SUUCESSFULLY "
            return render_template('confirmpg.html',msg=msg)

           

@app.route('/examreg',methods=['POST','GET'])        
def examreg():
    msg="msgin"
    if request.method == 'POST'  :
            subject=request.form['subject']
            subcode=request.form['subcode']
            exam_date=request.form['exam_date']
            reg_no=request.form['reg_no']
            stname=request.form['stname']
            dbHandler.insertexamreg(subject,subcode,exam_date,reg_no,stname)
            examregister=dbHandler.retriveex(reg_no)
            msg="RECORDS ADDED SUCCESSFULLY"
            con=sql.connect("database.db")
            con.row_factory=sql.Row

            cur=con.cursor()
            rows=cur.execute('select * from exam where reg_no=?',(reg_no,))
            return render_template('ack.html',msg=msg, rows=rows)
    else:        
            msg="RECORDS CANNOT BE EXEUTED SUUCESSFULLY "
            return render_template('confirmpg.html',msg=msg) 

@app.route('/viewstudentdetails')
def viewstudentdetails():
    
    con=sql.connect("database.db")
    con.row_factory=sql.Row

    cur=con.cursor()
    cur.execute('select * from students')
    rows=cur.fetchall()

    return render_template('viewstudentdetails.html',rows=rows)                    

@app.route('/viewexamdetails')
def viewexamdetails():
    con=sql.connect("database.db")
    con.row_factory=sql.Row

    cur=con.cursor()
    rows=cur.execute('select * from exam ')

    return render_template('viewexamdetails.html',rows=rows)

if __name__ == '__main__' :
        
        app.run(debug=True)
