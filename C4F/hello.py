from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route('/login/<username>/<password>')
def login(username, password):
    if password == 'Secret':
        return render_template('login.html', username=username, password=password)
    else:
        return 'Wrong password'
