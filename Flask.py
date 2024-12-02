'''
Author: Ms Rya
Version: 3.10
'''

from flask import *

app = Flask(__name__)

@app.route("/Admin")
def hello_admin():
    return "<h1>This is AdminPage</h1>"

@app.route("/display", methods=['POST'])
def f1():
    pname = request.form['n1']
    pid = request.form['n2']
    pcost = request.form['n3']
    tax = int(float(pcost)) * 0.18
    total = int(float(pcost)) + tax
    s = f'<h2><font color="blue">This is <b><font color="green">{pname}</font></b> details</h2></font>'
    s += f"<p>Product ID: {pid}</p>"
    s += f"<p>Product Cost: {pcost}</p>"
    s += f"<p>Tax: {tax}</p>"
    s += f"<p>Total Cost: {total}</p>"
    return s  

@app.route("/Home")
def f2():
    return "Hello home"

@app.route("/")
def f3():
    return render_template("A.html")

@app.route("/Contact")
def f4():
    return render_template("e.html", sname="Rya", sdept="CS")

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f"Welcome Guest {guest}!"

@app.route("/aboutus")
def about_us():
    return "<h1>About Us</h1><p>We are a small tech company.</p>"

@app.route('/display/<myvar>')
def f5(myvar):
    return render_template("e.html", sname=myvar, sdept="sci")

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

@app.route('/student/<Tutor>')
def fstudent(Tutor):
    return redirect(url_for('f5', myvar=Tutor))

if __name__ == '__main__':
    app.run(debug=True)
