from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from email_validator import validate_email

import os

# TODO switch emails
# TODO put on server
# TODO create requirements.txt
app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        try:
            valid_email = validate_email(email)
            email = valid_email.email
            send_email(name, email, message)
            flash('Email sent successfully. We will contact you soon!', category='success')
            return redirect(url_for('home_page'))
        except Exception as e:
            flash('Failed to send email. Please contact teri@theorchardon66.com.', category='error')
    return render_template('index.html')


def send_email(name, email, message):
    try:
        msg = Message(message,
                      sender=os.environ['SENDER'],
                      recipients=[os.environ['RECIPIENTS']])
        msg.body = f"Name: {name}\nEmail: {email}\nSubject: {message}"
        mail.send(msg)
    except Exception as e:
        raise e


if __name__ == '__main__':
    app.run()
