from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from email_validator import validate_email

import os
app = Flask(__name__)
app.secret_key = 'test'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'nataliehill1324@gmail.com'
app.config['MAIL_PASSWORD'] = 'brispkbjwkszlsx'
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        try:
            send_email(name, email, message)
            flash('Email sent successfully. We will contact you soon!', category='success')
            return redirect(url_for('home_page'))
        except Exception as e:
            flash('Failed to send email. Please contact teri@theorchardon66.com.', category='error')
    return render_template('index.html')


def send_email(name, email, message):
    try:
        msg = Message(message,
                      sender='nataliehill1324@gmail.com',
                      recipients=['nataliehill1324@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nSubject: {message}"
        mail.send(msg)
    except Exception as e:
        raise e
