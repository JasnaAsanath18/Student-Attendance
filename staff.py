from flask import *
from database import *
import uuid


staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staffhome():
    return render_template("staff_home.html")


@staff.route('/staff_view_student')
def staff_view_student():
    data={}
    q="select * from payment inner join fee using(fee_id)"
    data['py']=select(q)
    s="select * from student"
    res=select(s)
    data['res']=res
    return render_template("staff_view_student.html",data=data)

@staff.route('/staff_send_notification',methods=['get','post'])
def staff_send_notification():
    data={}
    s="select * from parent"
    data['parent']=select(s)
    if 'submit' in request.form:
        parent=request.form['pid']
        noti=request.form['noti']
        q="insert into fee_notification values(null,'%s','%s')"%(parent,noti)
        insert(q)
        flash("Notification Send")
        return redirect(url_for('staff.staff_send_notification'))
    return render_template("staff_send_notification.html",data=data)


@staff.route('/staff_manage_fee',methods=['get','post'])
def staff_manage_fee():
    data={}
    if 'sid' in request.args:
        session['sid']=request.args['sid']
    p="select * from fee where student_id='%s'"%(session['sid'])
    data['fee']=select(p)
    if 'submit' in request.form:
        fee=request.form['fee']
        amt=request.form['amt']
        date=request.form['date']
        a="insert into fee values(null,'%s','%s','%s','%s')"%(session['sid'],fee,amt,date)
        insert(a)
        flash("Fee Added")
        return redirect(url_for('staff.staff_manage_fee'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from fee where fee_id='%s'"%(id)
        delete(q)
        return redirect(url_for('staff.staff_manage_fee'))

    if action=='update':
        q="select * from fee where fee_id='%s'"%(id)
        print(q)
        res=select(q)
        print(res)
        data['res']=res
    
    if 'edit' in request.form:
        fee=request.form['fee'] 
        amt=request.form['amt']
        date=request.form['date']
        q="update fee set fee='%s',amount='%s',date='%s' where fee_id='%s'"%(fee,amt,date,id)
        update(q)
        return redirect(url_for('staff.staff_manage_fee'))
    return render_template("staff_manage_fee.html",data=data)

@staff.route('/staff_manage_payment')
def staff_manage_payment():
    sid=request.args['sid']
    data={}
    s="select *,payment.date as pdate from payment inner join fee using(fee_id) where student_id='%s'"%(sid)
    data['pay']=select(s)
    return render_template("staff_manage_payment.html",data=data)