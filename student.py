from flask import Flask,Blueprint,render_template,request,redirect,url_for,session
from database import *

student=Blueprint('student',__name__)

@student.route('/studenthome')
def studenthome():
    return render_template("studentlogin.html")

@student.route('/viewplan')
def viewplan():
    data={}
    s="select * from plan"
    res=select(s)
    data['res']=res
    '''
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='subscribe':
        q="insert into subscribe values(null,'%s','%s',"

    '''
    return render_template("viewplan.html",data=data)

@student.route('/viewsyllabus')
def viewsyllabus():
    data={}
    id=request.args['id']
    s="select * from syllabus where subject_id='%s'"%(id)
    print(s)
    rem=select(s)
    data['rem']=rem

    return render_template("viewsyllabus.html",data=data)


@student.route('/viewsubject')
def viewsubject():
    data={}
    s="select * from subject"
    res=select(s)
    data['res']=res

    return render_template("viewsubject.html",data=data)

@student.route('/viewvideo')
def viewvideo():
    data={}
    id=request.args['id']
    s="select * from videos where subject_id='%s'"%(id)
    res=select(s)
    data['res']=res
        
    return render_template("viewvideo.html",data=data)

@student.route('/sendcomplaint',methods=['get','post'])
def sendcomplaint():
    data={}
    s="select * from complaint where student_id='%s'"%(session['sid'])
    res=select(s)
    data['res']=res
    if 'submit' in request.form:
        a=request.form['complaint']
        q="insert into complaint values(null,'%s','%s','pending',now())"%(session['sid'],a)
        print(q)
        insert(q)
        return redirect(url_for('student.sendcomplaint'))
    

    return render_template("sendcomplaint.html",data=data)

@student.route('/viewqp')
def viewqp():
    data={}
    s="select * from question"
    res=select(s)
    data['res']=res
    return render_template("viewqp.html",data=data)
    
