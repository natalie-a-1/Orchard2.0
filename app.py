from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
