from flask import Flask, render_template, redirect, request, jsonify, url_for
import sqlite3

# Create an instance of the Flask application
app = Flask(__name__)

# Home route: Displays the landing page for the application
@app.route('/')
def home():
    return render_template("index.html")

# Route for employee enrollment: Collects employee details via POST and saves them to the database
app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open("index.html").read())  # Load the HTML file

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve form data
    product_name = request.form['productName']
    product_id = request.form['productId']
    cost = float(request.form['cost'])
    quantity = int(request.form['quantity'])

    # Calculate totals
    total = cost * quantity
    tax = total * 0.18  # 18% tax
    grand_total = total + tax

    # Generate response
    return f"""
    <h2>Product Summary</h2>
    <p>Product Name: {product_name}</p>
    <p>Product ID: {product_id}</p>
    <p>Cost: {cost}</p>
    <p>Quantity: {quantity}</p>
    <p>Total: {total}</p>
    <p>Tax (18%): {tax}</p>
    <p>Grand Total: {grand_total}</p>
    <a href="/">Go Back</a>
    """
@app.route('/')
def index():
    return render_template_string(open("index.html").read())  # Load the HTML file

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve form data
    product_name = request.form['productName']
    product_id = request.form['productId']
    cost = float(request.form['cost'])
    quantity = int(request.form['quantity'])

    # Calculate totals
    total = cost * quantity
    tax = total * 0.18  # 18% tax
    grand_total = total + tax

    # Generate response
    return f"""
    <h2>Product Summary</h2>
    <p>Product Name: {product_name}</p>
    <p>Product ID: {product_id}</p>
    <p>Cost: {cost}</p>
    <p>Quantity: {quantity}</p>
    <p>Total: {total}</p>
    <p>Tax (18%): {tax}</p>
    <p>Grand Total: {grand_total}</p>
    <a href="/">Go Back</a>
    """

# Route to view all employee records: Displays a list of all employees from the database
@app.route("/view")
def view():
    con = sqlite3.connect("employee.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()
    cur.execute("SELECT * FROM emptable")
    rows = cur.fetchall()  
    con.close() 
    return render_template("view.html", rows=rows)

# Route to update employee department: Allows updating the department of an employee based on their ID
@app.route("/update", methods=['POST', 'GET'])
def update():
    if request.method == "POST" or request.method == "GET": 
        try:
            empid = request.form['id']
            dept = request.form['dept']
            with sqlite3.connect("employee.db") as con:
                cur = con.cursor()
                print("Updating department...")
                cur.execute("UPDATE emptable SET dept = ? WHERE id = ?", (dept, empid))
                con.commit() 
                print("Update successful")
                return redirect(url_for('view'))
        except Exception as e:
            msg = f"Error while updating: {str(e)}"  
            return render_template("update.html", msg=msg)
    
    return render_template("update.html")

# Route to return employee data in JSON format: Fetches and returns all employee records as JSON
@app.route("/data")
def data():
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM emptable")
    rows = cur.fetchall()  
    con.close()  
    return jsonify(rows)

@app.route("/delete", methods=['POST', 'GET'])
def delete():
    msg = ""
    if request.method == "POST":  # Check if the form was submitted (POST request)
        empid = request.form['id']

    try: # It connects to the database now to delete the record with the given empID
        with sqlite3.connect("employee.db") as con:
                cursor = con.cursor()
                cursor.execute("DELETE FROM emptable WHERE id = ?", (empid,))
                con.commit()
                return redirect(url_for('view'))
    except Exception as e: 
        msg = f"Error while deleting: {str(e)}"  
        print(msg)
        return redirect(url_for('view'))  # Redirects to the employee list page if an error occurs
    
# Main entry point for the Flask application
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, redirect, request, jsonify, url_for
import sqlite3

# Create an instance of the Flask application
app = Flask(__name__)

# Home route: Displays the landing page for the application
@app.route('/')
def home():
    return render_template("index.html")

# Route for employee enrollment: Collects employee details via POST and saves them to the database
@app.route('/enroll', methods=['POST', 'GET'])
def empdetails():
    msg = ""  
    if request.method == "POST":  
        try:
            id = request.form['id']
            name = request.form['name']
            dept = request.form['dept']
            city = request.form['city']
            salary = request.form['salary']
            print(id, name, dept, city, salary)
            
            with sqlite3.connect("employee.db") as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO emptable(id, name, dept, city, salary) VALUES (?, ?, ?, ?, ?)",
                               (id, name, dept, city, salary))
                con.commit()  # Commit the transaction
                msg = "Saved successfully" 
                print(msg)
        except Exception as e:
            msg = f"Error while saving the data: {str(e)}"  

    return render_template("enroll.html", msg=msg)

# Route to view all employee records: Displays a list of all employees from the database
@app.route("/view")
def view():
    con = sqlite3.connect("employee.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()
    cur.execute("SELECT * FROM emptable")
    rows = cur.fetchall()  
    con.close() 
    return render_template("view.html", rows=rows)

# Route to update employee department: Allows updating the department of an employee based on their ID
@app.route("/update", methods=['POST', 'GET'])
def update():
    if request.method == "POST" or request.method == "GET": 
        try:
            empid = request.form['id']
            dept = request.form['dept']
            with sqlite3.connect("employee.db") as con:
                cur = con.cursor()
                print("Updating department...")
                cur.execute("UPDATE emptable SET dept = ? WHERE id = ?", (dept, empid))
                con.commit() 
                print("Update successful")
                return redirect(url_for('view'))
        except Exception as e:
            msg = f"Error while updating: {str(e)}"  
            return render_template("update.html", msg=msg)
    
    return render_template("update.html")

# Route to return employee data in JSON format: Fetches and returns all employee records as JSON
@app.route("/data")
def data():
    con = sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM emptable")
    rows = cur.fetchall()  
    con.close()  
    return jsonify(rows)

@app.route("/delete", methods=['POST', 'GET'])
def delete():
    msg = ""
    if request.method == "POST":  # Check if the form was submitted (POST request)
        empid = request.form['id']

    try: # It connects to the database now to delete the record with the given empID
        with sqlite3.connect("employee.db") as con:
                cursor = con.cursor()
                cursor.execute("DELETE FROM emptable WHERE id = ?", (empid,))
                con.commit()
                return redirect(url_for('view'))
    except Exception as e: 
        msg = f"Error while deleting: {str(e)}"  
        print(msg)
        return redirect(url_for('view'))  # Redirects to the employee list page if an error occurs
    
# Main entry point for the Flask application
if __name__ == "__main__":
    app.run(debug=True)
