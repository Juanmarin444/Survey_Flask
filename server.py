from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    first_name = request.form['first_name']
    print(first_name)

    last_name = request.form['last_name']
    print(last_name)

    location = request.form['location']
    print(location)

    comment = request.form['comment']
    print(comment)

    return render_template('result.html', first_name=first_name, last_name=last_name, location=location, comment=comment)
app.run(debug=True)