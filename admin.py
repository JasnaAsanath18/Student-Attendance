from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminlogin')
def adminlogin():
    return render_template("adminhome.html")

@admin.route('/manageteacher',methods=['get','post'])
def manageteacher():
    data={}
    s="select * from teacher inner join login using (login_id)"
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
        h=request.form['designation']
        i=request.form['qualification']
        print(a,b,c,d,e,f,g,h,i)
        r="insert into login values(null,'%s','%s','teacher')"%(c,d)
        lid=insert(r)
        q="insert into teacher values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,a,b,e,f,g,h,i)
        insert(q)
       
        return redirect(url_for('admin.manageteacher'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from teacher where login_id='%s'"%(id)
        delete(q)
        r="delete from login where login_id='%s'"%(id)
        delete(r)
        return redirect(url_for('admin.manageteacher'))

    if action=='update':
        q="select * from teacher where login_id='%s'"%(id)
        res=select(q)
        data['res']=res

    if 'edit' in request.form:
        a=request.form['fname']
        b=request.form['lname']
        e=request.form['place']
        f=request.form['phone']
        g=request.form['email']
        h=request.form['designation']
        i=request.form['qualification']
        print(a,b,e,f,g,h,i)
        r="update teacher set fname='%s',lname='%s',place='%s',phone='%s',email='%s',designation='%s',qualification='%s' where login_id='%s'"%(a,b,e,f,g,h,i,id)
        update(r)
        return redirect(url_for('admin.manageteacher'))
        
    return render_template("admin_manageteacher.html",data=data)

@admin.route('/admin_assign_teacher',methods=['get','post'])
def admin_assign_teacher():
     tid=request.args['id']
     data={}
     q="select * from subject"
     data['res']=select(q)
     if 'submit' in request.form:
          sub=request.form['sub']
          q="insert into assign_teacher values(null,'%s','%s')"%(tid,sub)
          insert(q)
          flash("Assigned")
     return render_template("admin_assign_teacher.html",data=data)

@admin.route('/admin_manage_staff',methods=['get','post'])
def admin_manage_staff():
    data={}
    s="select * from staff inner join login using (login_id)"
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
        r="insert into login values(null,'%s','%s','staff')"%(c,d)
        lid=insert(r)
        q="insert into staff values(null,'%s','%s','%s','%s','%s','%s')"%(lid,a,b,e,f,g)
        insert(q)
       
        return redirect(url_for('admin.admin_manage_staff'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from staff where login_id='%s'"%(id)
        delete(q)
        r="delete from login where login_id='%s'"%(id)
        delete(r)
        return redirect(url_for('admin.admin_manage_staff'))
    if action=='update':
        q="select * from staff where login_id='%s'"%(id)
        res=select(q)
        data['res']=res

    if 'edit' in request.form:
        a=request.form['fname']
        b=request.form['lname']
        e=request.form['place']
        f=request.form['phone']
        g=request.form['email']

        print(a,b,e,f,g)
        r="update teacher set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where login_id='%s'"%(a,b,e,f,g,id)
        update(r)
        return redirect(url_for('admin.admin_manage_staff'))
        
    return render_template("admin_manage_staff.html",data=data)

@admin.route('/managesubject',methods=['get','post'])
def managesubject():
    data={}
    s="select * from subject"
    res=select(s)
    data['sbjt']=res
    if 'addsubject' in request.form:
        a=request.form['subject']
        print(a)
        q="insert into subject values(null,'%s')"%(a)
        insert(q)
        return redirect(url_for('admin.managesubject'))

    if 'action' in request.args:
        action=request.args[
            
            'action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from subject where subject_id='%s'"%(id)
        delete(q)
        return redirect(url_for('admin.managesubject'))

    if action=='update':
        q="select * from subject where subject_id='%s'"%(id)
        print(q)
        res=select(q)
        print(res)
        data['res']=res
    
    if 'edit' in request.form:
        a=request.form['subject']
        print(a)
        q="update subject set subject='%s' where subject_id='%s'"%(a,id)
        update(q)
        return redirect(url_for('admin.managesubject'))

    return render_template("admin_managesubject.html",data=data)



@admin.route('/admin_view_student',methods=['get','post'])
def admin_view_student():
    data={}
    s="select * from student"
    res=select(s)
    data['res']=res
    if 'action' in request.args:
        action=request.args['action']
        sid=request.args['sid']
    else:
        action=None
    if action=='attendance':
        
        p="SELECT * FROM attendance INNER JOIN student USING(student_id) WHERE attendance.student_id='%s'"%(sid)
        data['atd']=select(p)
        data['check']=0       
    return render_template("admin_view_student.html",data=data)


@admin.route('/admin_view_report',methods=['post','get'])	
def admin_view_report():
	data={}
	if "sale" in request.form:
		yearly=request.form['yearly']
        
		if request.form['monthly']=="":
			monthly=""
		else:
			monthly=request.form['monthly']+'%'
		print(monthly)
		customer=request.form['student']	
		q="SELECT * FROM `attendance` INNER JOIN `student` USING (`student_id`) INNER JOIN `parent` USING (`student_id`) WHERE (`fname` LIKE '%s') OR (`date` LIKE '%s'  ) OR (`date` LIKE '%s' ) "%(customer,yearly,monthly)
		res=select(q)
		print(q)
		data['report']=res
		session['res']=res
		r=session['res']
	else:
		q="SELECT * FROM `attendance` INNER JOIN `student` USING (`student_id`) INNER JOIN `parent` USING (`student_id`)"
		res=select(q)
		data['report']=res
		session['res']=res
	
	return render_template('admin_view_report.html',data=data)



# @admin.route('/managesyllabus',methods=['get','post'])
# def managesyllabus():
#     data={}
#     q="select * from subject"
#     res=select(q)
#     data['sbj']=res
#     if 'submit' in request.form:
#         a=request.form['subject']
#         b=request.form['details']
#         c=request.files['file']
#         path='static/'+str(uuid.uuid4())+c.filename
#         c.save(path)
#         q="insert into syllabus values(null,'%s','%s','%s')"%(a,b,path)
#         insert(q)
#         return redirect(url_for('admin.managesyllabus'))
        


#     return render_template("managesyllabus.html",data=data)


# @admin.route('/manageplan',methods=['get','post'])
# def manageplan():
#     if 'submit' in request.form:
#         a=request.form['plan']
#         b=request.form['rate']
#         q="insert into plan values(null,'%s','%s')"%(a,b)
#         insert(q)
#         return redirect(url_for('admin.manageplan'))
#     return render_template("manageplan.html")

# @admin.route('/viewcomplaint',methods=['get','post'])
# def viewcomplaint():
#     data={}
#     s="select * from complaint"
#     res=select(s)
#     data['res']=res
#     if 'action' in request.args:
#         action=request.args['action']
#         id=request.args['id']
#     else:
#         action=None
#     if action=='reply':
#         data['check']=0
#     if 'replay' in request.form:
#         reply=request.form['reply']

#         q="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
#         update(q)
#         return redirect(url_for('admin.viewcomplaint'))
        
#     return render_template("viewcomplaint.html",data=data)
