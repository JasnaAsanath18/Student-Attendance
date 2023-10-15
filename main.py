from flask import Flask
from public import public
from admin import admin
from api import api
from teacher import teacher
from staff import staff

app=Flask(__name__)
from flask_mail import Mail
import smtplib
from email.mime.text import MIMEText

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(api,url_prefix="/api")
app.register_blueprint(teacher)
app.register_blueprint(staff)

mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'projectsriss2020@gmail.com'
app.config['MAIL_PASSWORD'] = 'vroiyiwujcvnvade'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.secret_key='key'

app.run(debug=True,port=5004,host="0.0.0.0")

