from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)

app.secret_key = "secret"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank.")
        print("First name cannot be blank.")
        return redirect('/')
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be blank.")
        print("Last name cannot be blank.")
        return redirect('/')
    if len(request.form['email']) < 1:
        flash("Email cannot be blank.")
        print("Email cannot be blank.")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.")
        print("Invalid email address.")
        return redirect('/')
    else:
        return render_template('result.html')
app.run(debug=True)