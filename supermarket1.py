from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    product_name = request.form['product_name']
    product_id = request.form['product_id']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    
    total_cost = price * quantity
    tax = total_cost * 0.18
    final_price = total_cost + tax
    
    return render_template('summary.html', product_name=product_name, product_id=product_id, total_cost=total_cost, tax=tax, final_price=final_price)

if __name__ == '__main__':
    app.run(debug=True)
