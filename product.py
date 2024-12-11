'''
Author: Ms Rya
Version: 3.10
'''
from flask import *

app = Flask(__name__)

@app.route('/')
def enrollment_form():
    return render_template('enrollment.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    code = request.form['code']
    cost = float(request.form['cost'])
    quantity = int(request.form['quantity'])

    total = cost * quantity
    tax = total * 0.18
    gross_pay = total + tax
    return render_template('display.html', name=name, code=code, cost=cost, quantity=quantity, total=total, tax=tax, gross_pay=gross_pay)

if __name__ == '__main__':
    app.run(debug=True)
