from flask import *
from database import *
import uuid

api=Blueprint('api',__name__)


@api.route('/login',methods=['get','post'])
def login():
    data={}
    uname=request.args['username']
    paswd=request.args['password']
    qry="select * from login where `username` ='%s' and `password`='%s'"%(uname,paswd)
    login=select(qry)
    if login:
        login_id=login[0]['login_id']
        if login[0]['user_type']=="student":
            qry="select * from student where login_id='%s'"%(login_id)
            deta=select(qry)
            if deta:
                data['student_id']=deta[0]['student_id']
                data['status']="success"
                data['check']=login
            else:
                data['status']="failed"
        if login[0]['user_type']=="parent":
            qry="select * from parent where login_id='%s'"%(login_id)
            deta=select(qry)
            if deta:
                data['parent_id']=deta[0]['parent_id']
                data['status']="success"
                data['check']=login
            else:
                data['status']="failed"
    return str(data)




@api.route('/student_view_attendance')
def student_view_attendance():
    data={}
    sid=request.args['student_id']
    qry="SELECT *,concat(teacher.fname,' ',teacher.lname) AS teachername FROM attendance INNER JOIN teacher USING(teacher_id) WHERE student_id='%s'"%(sid)
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)

@api.route('/student_view_notes')
def student_view_notes():
    data={}
    qry="SELECT *,concat(teacher.fname,' ',teacher.lname) AS teachername FROM notes INNER JOIN teacher USING(teacher_id) inner join subject using(subject_id)"
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)


@api.route('/student_view_notification')
def student_view_notification():
    data={}
    qry="SELECT * FROM notification "
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)



@api.route('/student_view_qp')
def student_view_qp():
    data={}
    qry="SELECT *,concat(teacher.fname,' ',teacher.lname) AS teachername FROM questionpaper inner join teacher using(teacher_id) inner join subject using(subject_id)"
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)



@api.route('/student_view_mark')
def student_view_mark():
    data={}
    sid=request.args['student_id']
    qry="SELECT *,concat(teacher.fname,' ',teacher.lname) AS teachername FROM marks INNER JOIN teacher USING(teacher_id)inner join subject using(subject_id) WHERE student_id='%s'"%(sid)
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)



@api.route('/student_view_studymaterial')
def student_view_studymaterial():
    data={}
    # sid=request.args['student_id']
    qry="SELECT *,concat(teacher.fname,' ',teacher.lname) AS teachername FROM sm INNER JOIN teacher USING(teacher_id)inner join subject using(subject_id)"
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)


@api.route('/parent_view_student')
def parent_view_student():
    data={}
    pid=request.args['parent_id']
    print(pid)
    qry="SELECT *,concat(student.fname,' ',student.lname) AS name FROM student inner join parent using(student_id) where parent_id='%s'"%(pid)
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)


@api.route('/parent_view_attendance')
def parent_view_attendance():
    data={}
    pid=request.args['parent_id']
    print(pid)
    qry="SELECT *,CONCAT(teacher.fname,' ',teacher.lname) AS teachername,CONCAT(student.fname,' ',student.lname) AS NAME FROM attendance INNER JOIN student USING(student_id) INNER JOIN parent USING(student_id) INNER JOIN teacher USING(teacher_id) where parent_id='%s'"%(pid)
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)



@api.route('/parent_view_mark')
def parent_view_mark():
    data={}
    pid=request.args['parent_id']
    print(pid)
    qry="SELECT *,CONCAT(teacher.fname,' ',teacher.lname) AS teachername FROM marks INNER JOIN student USING(student_id) INNER JOIN parent USING(student_id) INNER JOIN teacher USING(teacher_id)inner join subject using(subject_id) where parent_id='%s'"%(pid)
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)

@api.route('/parent_view_notification')
def parent_view_notification():
    data={}
    pid=request.args['parent_id']
    print(pid)
    qry="SELECT * FROM fee_notification where parent_id='%s'"%(pid)
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)


@api.route('/parent_view_fee')
def parent_view_fee():
    data={}
    pid=request.args['parent_id']
    print(pid)
    qry="SELECT * FROM fee INNER JOIN student USING (student_id)INNER JOIN parent USING(student_id) where parent_id='%s'"%(pid)
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)



@api.route('/parent_view_teacher')
def parent_view_teacher():
    data={}
    # pid=request.args['parent_id']
    # print(pid)
    qry="SELECT *,CONCAT(teacher.fname,' ',teacher.lname) AS teachername FROM teacher"
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)
@api.route('/student_view_teacher')
def student_view_teacher():
    data={}
    # pid=request.args['parent_id']
    # print(pid)
    qry="SELECT *,CONCAT(teacher.fname,' ',teacher.lname) AS teachername FROM teacher"
    res=select(qry)
    if res:
                data['status']="success"
                data['check']=res
    else:
                data['status']="failed"
    return str(data)


@api.route('/parent_pay_fee')
def parent_pay_fee():
    data={}
    feeid=request.args['fid']
    amount=request.args['amount']
    qry="insert into payment values(null,'%s','%s',curdate())"%(feeid,amount)
    res=insert(qry)
    if res:
        data['status']="success"
              
    else:
        data['status']="failed"
    return str(data)

@api.route('/chat_with_student', methods=['get', 'post'])
def chat_with_student():
    data = {}
    logid = request.args['logid']
    x="select * from student where student_id='%s'"%(logid)
    st=select(x)
    stlogin=st[0]['login_id']
    mg = request.args['mg']
    tid=request.args['tid']
    print(logid,stlogin,tid)
    q = "INSERT INTO `chats` VALUES(NULL,'%s','student','%s','teacher','%s',CURDATE())" % (logid,tid,mg)
    insert(q)
    print(q)
    data['status'] = 'success'
    data['method'] = 'chat'
    return str(data)


@api.route('/view_chat_with_student')
def view_chat_with_student():
    data = {}
    logid = request.args['logid']
    x="select * from student where student_id='%s'"%(logid)
    st=select(x)
    stlogin=st[0]['login_id']
    tid=request.args['tid']
    q = "SELECT * FROM `chats` WHERE (sender_id='%s' and reciever_id='%s')or(sender_id='%s' and reciever_id='%s')  ORDER BY `date_time` DESC" % (logid,tid,tid,logid)
    print(q)
    res=select(q)
    if res:
        data['data'] = res
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
    data['method'] = 'chatdetail'
    return str(data)

@api.route('/chat_with_parent', methods=['get', 'post'])
def chat_with_parent():
    data = {}
    logid = request.args['logid']
    x="select * from parent where parent_id='%s'"%(logid)
    st=select(x)
    # stlogin=st[0]['login_id']
    mg = request.args['mg']
    tid=request.args['tid']
    q = "INSERT INTO `chats` VALUES(NULL,'%s','parent','%s','teacher','%s',CURDATE())" % (logid,tid,mg)
    insert(q)
    data['status'] = 'success'
    data['method'] = 'chat'
    return str(data)


@api.route('/view_chat_with_parent')
def view_chat_with_parent():
    data = {}
    logid = request.args['logid']
    x="select * from parent where parent_id='%s'"%(logid)
    st=select(x)
    # stlogin=st[0]['login_id']
    tid=request.args['tid']
    q = "SELECT * FROM `chats` WHERE (sender_id='%s' and reciever_id='%s')or(sender_id='%s' and reciever_id='%s') ORDER BY `date_time` DESC" % (logid,tid,tid,logid)
    print(q)
    res=select(q)
    if res:
        data['data'] = res
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
    data['method'] = 'chatdetail'
    return str(data)


@api.route('/view_student_location')
def view_student_location():
    data = {}
    logid = request.args['login_id']
    q = "SELECT * FROM `location` inner join student using(student_id)  WHERE `student_id`=(SELECT `student_id` FROM `parent` WHERE `parent_id`='%s') ORDER BY `date_time` DESC" % (logid)
    res = select(q)
    if res:
        data['check'] = res
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
    return str(data)

@api.route('/update_location')
def update_location():
    data = {}
    lati = request.args['lati']
    longi = request.args['longi']
    driverid = request.args['student_id']
    q="UPDATE `location` SET `latitude`='%s',`longitude`='%s' WHERE `student_id`='%s' " % (lati,longi,driverid)
    res=update(q)
    if res:
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
    return str(data)



@api.route('/parent_view_location')
def parent_view_location():
       data={}
       pid=request.args['parent_id']
       s="select * from location inner join student using(student_id) where student_id=(SELECT `student_id` FROM `parent` WHERE `parent_id`='%s')"%(pid)
       res = select(s)
       if res:
            data['check'] = res
            data['status'] = 'success'
       else:
            data['status'] = 'failed'
       return str(data)