import get
from datetime import datetime
from flask import Flask, render_template, request, session, flash
from textblob import TextBlob
import t

app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root4646",
  database="vtpai07_2021"
)

mycursor = mydb.cursor()
app.secret_key = 'your secret key'

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/user')
def user():
    cursor = mydb.cursor()
    cursor.execute('SELECT name FROM company')
    com = cursor.fetchall()
    return render_template('user.html', result = com)

@app.route('/reg')
def reg():
    cursor = mydb.cursor()
    cursor.execute('SELECT name FROM company')
    com = cursor.fetchall()
    return render_template('reg.html', result = com)

@app.route('/comp')
def comp():
    return render_template('comp.html')

@app.route('/creg')
def creg():
    return render_template('creg.html')

@app.route('/ahome')
def ahome():
    return render_template('ahome.html')

@app.route('/uhome')
def uhome():
    name = session['name']
    return render_template('uhome.html', result = name)

@app.route('/chome')
def chome():
    com = session['com']
    return render_template('chome.html', result = com)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html')

@app.route('/addprod')
def addprod():
    return render_template('addprod.html')

@app.route('/usearch')
def usearch():
    return render_template('usearch.html')

@app.route('/alogin', methods = ['POST', 'GET'])
def alogin():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pwd']
        if uname == 'admin' and pwd == 'admin':
            return render_template('ahome.html')
        else:
            return render_template('admin.html')

@app.route('/ulogin', methods = ['POST', 'GET'])
def ulogin():
    if request.method == 'POST':
        uid = request.form['uid']
        pwd = request.form['pwd']
        com = request.form['com']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s and company = %s and sta = %s', (uid, pwd, com, 'Approved'))
        account = cursor.fetchone()
        if account:
            session['uid'] = request.form['uid']
            session['ud'] = account[8]
            session['name'] = account[0]
            session['com'] = com
            return render_template('uhome.html', result = account[0])
        else:
            cursor = mydb.cursor()
            cursor.execute('SELECT name FROM company')
            com = cursor.fetchall()
            return render_template('user.html', result = com)

@app.route('/ureg', methods = ['POST', 'GET'])
def ureg():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        uid = request.form['uid']
        pwd = request.form['pwd']
        mob = request.form['mob']
        loc = request.form['loc']
        com = request.form['com']
        var = (fname, lname, uid, pwd, mob, loc, com, 'pending', 'id')
        cursor = mydb.cursor()
        cursor.execute('select * from user where email = %s and company = %s', (uid, com))
        d = cursor.fetchone()
        if d:
            flash("User Already Exists, Please Login here...")
            cursor.execute('SELECT name FROM company')
            com = cursor.fetchall()
            return render_template('user.html', result = com)
        else:
            cursor.execute('insert into user values(%s, %s, %s, %s, %s, %s, %s, %s, %s)', var)
            mydb.commit()
            if cursor.rowcount == 1:
                cursor.execute('SELECT name FROM company')
                com = cursor.fetchall()
                return render_template('user.html', result = com)
            else:
                return render_template('reg.html')
        
@app.route('/clogin', methods = ['POST', 'GET'])
def clogin():
    if request.method == 'POST':
        uid = request.form['uid']
        pwd = request.form['pwd']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM company WHERE email = %s AND password = %s', (uid, pwd))
        account = cursor.fetchone()
        if account:
            session['uid'] = request.form['uid']
            session['com'] = account[0]
            return render_template('chome.html', result = account[0])
        else:
            return render_template('comp.html')

@app.route('/creg1', methods = ['POST', 'GET'])
def creg1():
    if request.method == 'POST':
        name = request.form['name']
        uid = request.form['uid']
        pwd = request.form['pwd']
        mob = request.form['mob']
        loc = request.form['loc']
        var = (name, uid, pwd, mob, loc)
        cursor = mydb.cursor()
        cursor.execute('insert into company values(%s, %s, %s, %s, %s)', var)
        mydb.commit()
        if cursor.rowcount == 1:
            return render_template('comp.html')
        else:
            return render_template('creg.html')
        
@app.route('/prod', methods = ['POST', 'GET'])
def prod():
    if request.method == 'POST':
        name = request.form['pname']
        mod = request.form['mod']
        fea = request.form['fea']
        price = request.form['price']
        qun = request.form['qun']
        com = session['com']
        var = (name, mod, fea, price, qun, com)
        cursor = mydb.cursor()
        cursor.execute('insert into product values(0, %s, %s, %s, %s, %s, %s)', var)
        mydb.commit()
        if cursor.rowcount == 1:
            return render_template('chome.html', result = com)
        else:
            return render_template('addprod.html')

@app.route('/auser')
def auser():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM user where sta="Approved"')
    data = cursor.fetchall()
    cursor.execute('SELECT * FROM user where sta="pending"')
    data1 = cursor.fetchall()
    return render_template('auser.html', result = data, result1 = data1)

@app.route('/agraph')
def agraph():
    return render_template('agraph.html')

@app.route('/aadd')
def aadd():
    query = request.args.getlist('uid')
    uid = get.getId()
    cursor = mydb.cursor()
    cursor.execute("update user set sta = %s, UID = %s where email = %s and company = %s", ('Approved', uid, query[0], query[1]))
    mydb.commit()
    if cursor.rowcount == 1:
        cursor.execute('SELECT * FROM user where sta="Approved"')
        data = cursor.fetchall()
        cursor.execute('SELECT * FROM user where sta="pending"')
        data1 = cursor.fetchall()
        return render_template('auser.html', result = data, result1 = data1)
    else:
        cursor.execute('SELECT * FROM user where sta="Approved"')
        data = cursor.fetchall()
        cursor.execute('SELECT * FROM user where sta="pending"')
        data1 = cursor.fetchall()
        return render_template('auser.html', result = data, result1 = data1)
    

@app.route('/acom')
def acom():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM company')
    data = cursor.fetchall()
    return render_template('acom.html', result = data)

@app.route('/aprod')
def aprod():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM product')
    data = cursor.fetchall()
    return render_template('aprod.html', result = data)

@app.route('/arev')
def arev():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM urev where sta="pending"')
    data = cursor.fetchall()
    print(data)
    return render_template('arev.html', result = data)

@app.route('/areq/<string:id>')
def areq(id):
    cursor = mydb.cursor()
    cursor.execute("update urev set sta = %s where id = %s", ('request', id))
    mydb.commit()
    if cursor.rowcount == 1:
        print("Hello")
        cursor.execute('SELECT * FROM urev where sta="pending"')
        data = cursor.fetchall()
        return render_template('arev.html', result = data)
    else:
        cursor.execute('SELECT * FROM urev where sta="pending"')
        data = cursor.fetchall()
        return render_template('arev.html', result = data)

@app.route('/uprod', methods = ['POST', 'GET'])
def uprod():
    if request.method == 'POST':
        pname = request.form['pname']
        com = session['com']
        cursor = mydb.cursor()
        cursor.execute("select * from product where name like '%"+pname+"%' and company ='"+com+"'")
        prod = cursor.fetchall()
        return render_template('uprod.html', result = prod)

@app.route('/ubuy/<string:id>')
def ubuy(id):
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM product where id='+id)
    data = cursor.fetchone()
    session['id'] = id
    return render_template('ubuy.html', result = data)

@app.route('/upbuy', methods = ['POST', 'GET'])
def upbuy():
    if request.method == 'POST':
        pid = session['id']
        qun = request.form['qun']
        com = session['com']
        uid = session['ud']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM product where id='+pid)
        data = cursor.fetchone()
        var = (data[1], data[2], data[3], data[4], qun, uid, com, pid, 'pending')
        cursor.execute('insert into ubuy values(0, %s, %s, %s, %s, %s, %s, %s, %s, %s)', var)
        mydb.commit()
        if cursor.rowcount == 1:
            name = session['name']
            return render_template('uhome.html', result = name)
        else:
            return render_template('ubuy.html', result = data)
    
@app.route('/udel')
def udel():
    uid = session['ud']
    com = session['com']
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM ubuy where uid=%s and company=%s and status=%s', (uid, com, 'Delivered'))
    data = cursor.fetchall()
    print(data)
    return render_template('udel.html', result = data)

@app.route('/prec/<string:id>')
def prec(id):
    session['id'] = id
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM ubuy where id='+id)
    data = cursor.fetchone()
    return render_template('prec.html', result = data)

@app.route('/uprec', methods= ['POST', 'GET'])
def uprec():
    if request.method == 'POST':
        pid = session['id']
        rev = request.form['rev']
        cursor = mydb.cursor()
        cursor.execute('SELECT pid FROM ubuy where id='+pid)
        data = cursor.fetchone()
        cursor.execute('select * from recommendation where pid="'+str(data[0])+'"')
        re = cursor.fetchall()
        mycursor.execute("select * from urev where uid=%s and pid =%s", (session['ud'], 
                                                                        data[0]))
        r = mycursor.fetchall()
        if len(r) == 0:
            mycursor.execute("insert into urev values(0, %s, %s, %s, %s)", (session['ud'], 
                                                                            data[0], rev, 'pending'))
            mydb.commit()
        if len(re) != 0:
            hcode = get.Hashgen()
            cursor.execute('select * from recommendation where pid="'+str(data[0])+'"')
            res = cursor.fetchall()
            for x in res:
                phcode = x[1]
            var = (hcode, rev, phcode, datetime.now(), data[0])
            cursor.execute('insert into recommendation values(0, %s, %s, %s, %s, %s)', var)
            mydb.commit()
            if cursor.rowcount == 1:
                name = session['name']
                return render_template('uhome.html', result = name)
            else:
                cursor.execute('SELECT * FROM ubuy where id='+pid)
                data = cursor.fetchone()
                return render_template('prec.html', result = data)
        else:
            hcode = get.Hashgen()
            var = (hcode, rev, 0, datetime.now(), data[0])
            cursor.execute('insert into recommendation values(0, %s, %s, %s, %s, %s)', var)
            mydb.commit()
            if cursor.rowcount == 1:
                name = session['name']
                return render_template('uhome.html', result = name)
            else:
                cursor.execute('SELECT * FROM ubuy where id='+pid)
                data = cursor.fetchone()
                return render_template('prec.html', result = data)
            
@app.route('/urec/<string:id>')
def urec(id):
    cursor = mydb.cursor()
    cursor.execute('select review from recommendation where pid="'+id+'"')
    re = cursor.fetchall()
    to = 0 
    p = 0
    n = 0
    nu = 0
    for x in re:
        print(x[0])
        to += 1
        analysis = TextBlob(x[0])
        sentiment = analysis.sentiment.polarity
        print("pol:", sentiment)
        if sentiment > 0:
            p += 1
        elif sentiment < 0:
            n += 1
        else:
            nu += 1
    name = [p, n, nu, to]
    cursor.execute("select name from product where id ='"+id+"'")
    d = cursor.fetchone()
    #ssl = t.reviewCount(d[0])
    return render_template('urec.html', result = name)

@app.route('/cprod')
def cprod():
    com = session['com']
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM ubuy where company=%s and status=%s', (com, 'pending'))
    data = cursor.fetchall()
    return render_template('cprod.html', result = data)

@app.route('/cbuy/<string:id>')
def cbuy(id):
    com = session['com']
    cursor = mydb.cursor()
    cursor.execute('update ubuy set status="Delivered" where id='+id)
    mydb.commit()
    if cursor.rowcount == 1:
        cursor.execute('SELECT * FROM ubuy where company=%s and status=%s', (com, 'pending'))
        data = cursor.fetchall()
        return render_template('cprod.html', result = data)
    else:
        cursor.execute('SELECT * FROM ubuy where company=%s and status=%s', (com, 'pending'))
        data = cursor.fetchall()
        return render_template('cprod.html', result = data)
    
@app.route('/urev')
def urev():
    uid = session['ud']
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM urev where sta='request' and Uid='"+uid+"'")
    data = cursor.fetchall()
    return render_template('urev.html', result = data)
    
@app.route('/ureq/<string:id>')
def ureq(id):
    cursor = mydb.cursor()
    cursor.execute("update urev set sta = %s where id = %s", ('Approved', id))
    mydb.commit()
    if cursor.rowcount == 1:
        l = [100, 150, 200, 250, 300, 500, 1000]
        import random
        ri = random.randint(0,len(l)-1)
        cursor.execute('insert into incent values(0, %s, %s, %s)', (session['ud'], l[ri], datetime.now()))
        mydb.commit()
        cursor.execute('SELECT * FROM urev where sta="request"')
        data = cursor.fetchall()
        return render_template('urev.html', result = data)
    else:
        cursor.execute('SELECT * FROM urev where sta="request"')
        data = cursor.fetchall()
        return render_template('urev.html', result = data)
    
@app.route('/uinc')
def uinc():
    uid = session['ud']
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM incent where Uid='"+uid+"'")
    data = cursor.fetchall()
    return render_template('uinc.html', result = data)
    
if __name__ == '__main__':
   app.run()