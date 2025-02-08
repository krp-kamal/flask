from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def f2():
	return render_template('d.html')
'''
@app.route("/enroll",methods= ['post'])
def f1():
	pname = request.form['p1']
	pid = request.form['p2']
	pcost = request.form['p3']
	pqty = request.form['p4']
	ptotal = int(pcost) * int(pqty)
	ptax = ptotal * 0.18
	pgs = ptotal + ptax
	return render_template('e.html',pN=pname,pI=pid,pC=pcost,tpgs=pgs)
'''
@app.route('/data')
def f3():
	d ={'k1':'v1','k2':['product1','product2','product3','product4'],'k3':{'k1':123}}
	return jsonify(d)

@app.route("/enroll",methods= ['post'])
def f1():
	pname = request.form['p1']
	pid = request.form['p2']
	pcost = request.form['p3']
	pqty = request.form['p4']
	ptotal = int(pcost) * int(pqty)
	ptax = ptotal * 0.18
	pgs = ptotal + ptax
	d = {'productname':pname,'Productinfo':[pid,pcost,pqty,ptotal,ptax,pgs]}
	return jsonify(d)

if __name__ == '__main__':
	app.run(debug=True)
