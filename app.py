from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    return render_template('home.html')


@app.route("/about")
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
