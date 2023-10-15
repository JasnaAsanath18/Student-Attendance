from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template("home.html")

@public.route('/login',methods=['get','post'])
def login():
    if 'login' in request.form:
        a=request.form['uname']
        b=request.form['password']
        print(a,b)
        q="select * from login where username='%s' and password='%s'"%(a,b)
        print(q)
        res=select(q)
        if res:
            session['lid']=res[0]['login_id']
            u_type=res[0]['user_type']

            if u_type=="admin":
                return redirect(url_for('admin.adminlogin'))
            if u_type=="staff":
                q="select * from staff where login_id='%s'"%(session['lid'])
                re=select(q)
                session['staffid']=re[0]['staff_id']
                return redirect(url_for('staff.staffhome'))
            
            elif u_type=="teacher":
                q="select * from teacher where login_id='%s'"%(session['lid'])
                re=select(q)
                session['tcr_id']=re[0]['teacher_id']
                return redirect(url_for('teacher.teacherlogin'))
            # elif u_type=="parent":
            #     q="select * from parent where login_id='%s'"%(session['lid'])
            #     re=select(q)
            #     session['parent_id']=re[0]['parent_id']
            #     return redirect(url_for('teacher.teacherlogin'))
            # elif u_type=="student":
            #     q="select * from student where login_id='%s'"%(session['lid'])
            #     re=select(q)
            #     session['sid']=re[0]['student_id']
            #     return redirect(url_for('student.studenthome'))
        else:
            flash("invalid login")
            return redirect(url_for('public.login'))
    return render_template("login.html")

@public.route('/register',methods=['get','post'])
def register():
    if 'register' in request.form:
        a=request.form['fname']
        b=request.form['lname']
        c=request.form['uname']
        d=request.form['password']
        e=request.form['place']
        f=request.form['phone']
        g=request.form['email']
        print(a,b,c,d,e,f,g)
        q="insert into login values(null,'%s','%s','student')"%(c,d)
        lid=insert(q)
        r="insert into student values(null,'%s','%s','%s','%s','%s','%s')"%(lid,a,b,e,f,g)
        insert(r)
        flash("Registration completed")
        return redirect(url_for('public.register'))
    return render_template("register.html")
