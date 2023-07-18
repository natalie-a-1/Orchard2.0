from flask import Flask, render_template
from flask import request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'nataliehill405@icloud.com'
app.config['MAIL_PASSWORD'] = 'Thunder2003$'
mail = Mail(app)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Extract form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    send_email(name, email, message)


def send_email(name, email, message):
    # Create the email message
    msg = Message(message,
                  recipients=['prestondjones7@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\nSubject: {message}"

    # Send the email
    mail.send(msg)


if __name__ == '__main__':
    app.run()
