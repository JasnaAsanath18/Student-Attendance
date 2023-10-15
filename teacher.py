import uuid
from flask import *
from database import *
import random


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

teacher=Blueprint('teacher',__name__)

@teacher.route('/teacherlogin')
def teacherlogin():
    return render_template("teacherhome.html")

@teacher.route('/teacher_viewsubject',methods=['get','post'])
def viewsubject():
    data={}
    s="select * from subject inner join assign_teacher using(subject_id) inner join teacher using(teacher_id) where teacher_id='%s'"%(session['tcr_id'])

    res=select(s)
    data['res']=res
    # if 'action' in request.args:
    #     action=request.args['action']
    #     id=request.args['id']
    # else:
    #     action=None
    # if action==  'addvideo':  
    #    data['check']=0

    # if 'submit' in request.form:
    #     a=request.files['video']
    #     path='static/'+str(uuid.uuid4())+a.filename
    #     a.save(path)
    #     q="insert into videos values(null,'%s','%s')"%(id,path)
    #     insert(q)
    #     return redirect(url_for('teacher.viewsubject'))
    return render_template("teacher_viewsubject.html",data=data)

@teacher.route('/teacher_viewsyllabus')
def viewsyllabus():
    data={}
    id=request.args['id']
    s="select * from syllabus where subject_id='%s'"%(id)
    print(s)
    rem=select(s)
    data['rem']=rem

    return render_template("teacher_viewsyllabus.html",data=data)

@teacher.route('/addqp',methods=['get','post'])
def addqp():
 
    data={}
    s="select * from subject inner join assign_teacher using(subject_id) where teacher_id='%s'"%(session['tcr_id'])
    data['sbj']=select(s)
    s="select * from questionpaper inner join subject using(subject_id)"
    res=select(s)
    data['res']=res
    if 'submit' in request.form:
        a=request.form['question']
        sub=request.form['sub']
        b=request.files['qp']
        path='static/'+str(uuid.uuid4())+b.filename
        b.save(path)
        q="insert into questionpaper values(null,'%s','%s','%s','%s',curdate())"%(session['tcr_id'],sub,path,a)
        insert(q)
        return redirect(url_for('teacher.addqp'))
    return render_template("teacher_manage_qp.html",data=data)

@teacher.route('/teacher_manage_note',methods=['get','post'])
def teacher_manage_note():
    data={}
    tid=session['tcr_id']
    x="select * from subject"
    data['sbj']=select(x)
    p="select * from notes inner join subject using(subject_id) where teacher_id='%s'"%(tid)
    data['note']=select(p)
    if 'submit' in request.form:
        note=request.files['note']
        path='static/notes/'+str(uuid.uuid4())+note.filename
        note.save(path)
        sub=request.form['sub']
        
        a="insert into notes values(null,'%s','%s','%s')"%(session['tcr_id'],path,sub)
        insert(a)
        flash("Notes Added")
        return redirect(url_for('teacher.teacher_manage_note'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from notes where note_id='%s'"%(id)
        delete(q)
        return redirect(url_for('teacher.teacher_manage_note'))

    if action=='update':
        q="select * from notes inner join subject using(subject_id) where note_id='%s'"%(id)
        print(q)
        res=select(q)
        print(res)
        data['res']=res
    
    if 'edit' in request.form:
        note=request.files['note']
        path='static/notes/'+str(uuid.uuid4()+note.filename)
        note.save(path)
        sub=request.form['sub']
        q="update notes set note='%s',subject_id='%s' where note_id='%s'"%(path,sub,id)
        update(q)
        return redirect(url_for('teacher.teacher_manage_note'))
    return render_template("teacher_manage_note.html",data=data)



@teacher.route('/teacher_manage_student',methods=['get','post'])
def teacher_manage_student():
    data={}
    
    s="select * from student inner join login using (login_id)"
    res=select(s)
    data['tcr']=res
    if 'submit' in request.form:
        a=request.form['fname']
        b=request.form['lname']
        c=request.form['uname']
        d=request.form['password']
        e=request.form['place']
        f=request.form['phone']
        g=request.form['email']
     
        print(a,b,c,d,e,f,g)
        r="insert into login values(null,'%s','%s','student')"%(c,d)
        lid=insert(r)
        q="insert into student values(null,'%s','%s','%s','%s','%s','%s')"%(lid,a,b,e,f,g)
        sid=insert(q)
        w="insert into location values(null,'%s',null,null,curdate())"%(sid)
        insert(w)
        flash("Student Added")
       
        return redirect(url_for('teacher.teacher_manage_student'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from student where login_id='%s'"%(id)
        delete(q)
        r="delete from login where login_id='%s'"%(id)
        delete(r)
        flash("Parent Removed")
        return redirect(url_for('teacher.teacher_manage_student'))

    if action=='update':
        q="select * from student where login_id='%s'"%(id)
        res=select(q)
        data['res']=res

    if 'edit' in request.form:
        a=request.form['fname']
        b=request.form['lname']
        e=request.form['place']
        f=request.form['phone']
        g=request.form['email']

        print(a,b,e,f,g)
        r="update student set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where login_id='%s'"%(a,b,e,f,g,id)
        update(r)
        return redirect(url_for('teacher.teacher_manage_student'))
        
    return render_template("teacher_manage_student.html",data=data)






@teacher.route('/teacher_add_parent',methods=['get','post'])
def teacher_manage_parent():
    if "sid" in request.args:  
        session['stid']=request.args['sid']
    data={}
    b="select * from parent  where student_id='%s'"%(session['stid'])
    res=select(b)
    if res:
        s="SELECT * FROM parent INNER JOIN student USING (student_id) INNER JOIN login ON parent.login_id=login.login_id  WHERE student_id='%s'"%(session['stid'])
        res=select(s)
        data['tcr']=res
    
    else:
        flash("Parent not added")
        data['check']=0   
        if 'submit' in request.form:
            a=request.form['fname']
            b=request.form['lname']
            c=request.form['uname']
            d=request.form['password']
            e=request.form['place']
            f=request.form['phone']
            g=request.form['email']
            print(a,b,c,d,e,f,g)
            r="insert into login values(null,'%s','%s','parent')"%(c,d)
            lid=insert(r)
            q="insert into parent values(null,'%s','%s','%s','%s','%s','%s','%s')"%(lid,a,b,e,f,g,session['stid'])
            insert(q)
            flash("Parent Added")
    
            return redirect(url_for('teacher.teacher_manage_student'))
        
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from parent where login_id='%s'"%(id)
        delete(q)
        r="delete from login where login_id='%s'"%(id)
        delete(r)
        return redirect(url_for('teacher.teacher_manage_student'))

    if action=='update':
        q="select * from parent where login_id='%s'"%(id)
        print(q)
        res=select(q)
        data['res']=res

    if 'edit' in request.form:
        a=request.form['fname']
        b=request.form['lname']
        e=request.form['place']
        f=request.form['phone']
        g=request.form['email']

        r="update parent set p_fname='%s',p_lname='%s',p_place='%s',p_phone='%s',p_email='%s' where login_id='%s'"%(a,b,e,f,g,id)
        update(r)
        return redirect(url_for('teacher.teacher_manage_parent'))
    
    return render_template("teacher_manage_parent.html",data=data)
   
@teacher.route("/chat_with_student",methods=['get','post'])
def chat_with_student():
    data={}
    s="select * from student"
    data['std']=select(s)
    return render_template("teacher_chat_with_student.html",data=data)

@teacher.route("/chat_student",methods=['get','post'])
def chat_student():
    data={}
    d_id=session['lid']
    data['d_id']=d_id
    id=request.args['id']
    q1="select * from chats where  (sender_id='%s' and reciever_id='%s') or (sender_id='%s' and reciever_id='%s') "%(d_id,id,id,d_id)
    res=select(q1)
    data['view']=res

    if 'submit' in request.form:
        msg=request.form['msg']
        q="insert into chats values(NULL,'%s','teacher','%s','student','%s',now())"%(d_id,id,msg)
        res=insert(q)
        print(res)
        return redirect(url_for("teacher.chat_student",id=id,d_id=d_id))
    return render_template("teacher_student_chat.html",data=data)

@teacher.route("/chat_with_parent",methods=['get','post'])
def chat_with_parent():
    data={}
    s="select * from parent"
    data['std']=select(s)
    return render_template("teacher_chat_with_parent.html",data=data)

@teacher.route("/chat_parent",methods=['get','post'])
def chat_parent():
    data={}
    d_id=session['lid']
    data['d_id']=d_id
    id=request.args['id']
    q1="select * from chats where  (sender_id='%s' and reciever_id='%s') or (sender_id='%s' and reciever_id='%s') "%(d_id,id,id,d_id)
    res=select(q1)
    data['view']=res

    if 'submit' in request.form:
        msg=request.form['msg']
        q="insert into chats values(NULL,'%s','teacher','%s','parent','%s',now())"%(d_id,id,msg)
        res=insert(q)
        print(res)
        return redirect(url_for("teacher.chat_parent",id=id,d_id=d_id))
    return render_template("teacher_parent_chat.html",data=data)


@teacher.route("/teacher_add_notification",methods=['get','post'])
def teacher_add_notification():
    if 'submit' in request.form:
        noti=request.form['notification']
        q="insert into notification values(null,'%s')"%(noti)
        insert(q)
        flash("notification send")
        return redirect(url_for('teacher.teacher_add_notification'))
    return render_template("teacher_add_notification.html")


@teacher.route("/teacher_manage_attendance",methods=['get','post'])
def teacher_manage_attendance():
    data={}
    if 'id' in request.args:
        session['sid']=sid=request.args['id']
    q="select * from attendance inner join student using(student_id) where student_id='%s'"%(session['sid'])
    data['atd']=select(q)
    if 'submit' in request.form:
        status=request.form['status']
        date=request.form['date']
        s="insert into attendance values(null,'%s','%s','%s','%s',now())"%(session['sid'],session['tcr_id'],status,date)
        insert(s)
        flash("Attendance Added")
        if status=='leave':
            r="SELECT *,CONCAT(student.fname,' ',student.lname)AS `stu_name` FROM student INNER JOIN parent USING(student_id) INNER JOIN attendance USING(student_id) where student_id='%s'"%(session['sid'])
            parent=select(r)
            parent_mail=parent[0]['p_email']
            name=parent[0]['stu_name']
            stat=parent[0]['date']


            ############################
            rd=random.randrange(1000,9999,4)
			# msg=str(rd)
            msg="your Child '%s' is absent on'%s'"%(name,stat)
            data['rd']=rd
            print(rd)
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('projectsriss2020@gmail.com','vroiyiwujcvnvade')
            except Exception as ex:
                print("Couldn't setup email!!"+str(ex))
            msg = MIMEText(msg)
            
            msg['Subject'] = 'Attendance Report'
            
            msg['To'] = parent_mail
            
            msg['From'] = 'projectsriss2020@gmail.com'
            
            try:
                gmail.send_message(msg)
                print(msg)
				# flash("EMAIL SENED SUCCESFULLY")
                session['rd']=rd
				# return redirect(url_for('public.enterotp'))
                return redirect(url_for('teacher.teacher_manage_attendance'))
            except Exception as ex:
                print("COULDN'T SEND EMAIL", str(ex))
				# return redirect(url_for('public.forgotpassword'))
                return redirect(url_for('teacher.teacher_manage_attendance'))
				################################

        return redirect(url_for('teacher.teacher_manage_student',sid=sid))
    return render_template("teacher_manage_attendance.html",data=data)



@teacher.route("/teacher_view_location",methods=['get','post'])
def teacher_view_location():
    data={}
    sid=request.args['id']
    s="select * from location inner join student using (student_id) where student_id='%s'"%(sid)
    data['loc']=select(s)

 
    return render_template("teacher_view_location.html",data=data)


@teacher.route("/teacher_manage_exammark",methods=['get','post'])
def teacher_manage_exammark():
    sid=request.args['id']
    data={}
    e="select * from marks inner join subject using(subject_id) inner join student using(student_id) where student_id='%s' and teacher_id='%s'"%(sid,session['tcr_id'])
    s="select * from subject inner join assign_teacher using(subject_id) where teacher_id='%s'"%(session['tcr_id'])
    data['mark']=select(e)
    data['sbj']=select(s)
    if 'submit' in request.form:
        sub=request.form['sub']
        mark=request.form['mark']
        s="insert into marks values(null,'%s','%s','%s','%s')"%(session['tcr_id'],sid,sub,mark)
        insert(s)
        flash("Mark Added")
        return redirect(url_for('teacher.teacher_manage_student'))
    return render_template("teacher_manage_exammark.html",data=data)





@teacher.route("/teacher_manage_sm",methods=['get','post'])
def teacher_manage_sm():

    data={}
    s="select * from subject inner join assign_teacher using(subject_id) where teacher_id='%s'"%(session['tcr_id'])
    data['sbj']=select(s)
    s="select * from sm inner join subject using(subject_id)"
    data['res']=select(s)
    if 'submit' in request.form:
        sub=request.form['sub']
        title=request.form['title']
        det=request.form['det']
        s="insert into sm values(null,'%s','%s','%s','%s')"%(session['tcr_id'],sub,title,det)
        insert(s)
        flash("Study Material Added")
        return redirect(url_for('teacher.teacher_manage_sm'))
    return render_template("teacher_manage_sm.html",data=data)