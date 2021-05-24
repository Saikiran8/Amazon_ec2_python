from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'Saiki'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Saiki@123_'
app.config['MYSQL_DATABASE_DB'] = 'IoTBox'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()


@app.route('/home')
def open():
    return render_template("home.html")


@app.route('/')
def home():
    try:
        cur = conn.cursor()
        cur.execute("select measuredTemp from board where boardID='1';")
        fetchdata = cur.fetchall()
        cur.close()
    except Exception as e:
        print(e)
    return '{"2":"'+str(fetchdata[0][0])+'"}'


@app.route('/lidStatus')
def lid_status():
    lid = request.args.get('status')
    if lid == '1':
        try:
            cur = conn.cursor()
            cur.execute("update board set lidStatus='1' where boardID='1';")
            cur.close()
            print("ON")
        except Exception as e:
            print(e)
        return '''<h1>LID OPENED</h1>'''
    elif lid == '0':
        try:
            cur = conn.cursor()
            cur.execute("update board set lidStatus='0' where boardID='1';")
            cur.close()
            print("OFF")
        except Exception as e:
            print(e)
        return '''<h1>LID CLOSED</h1>'''
    else:
        print("wrong Implementation")
        return '''<h1>WRONG OPERATION</h1>'''


@app.route('/led1')
def ledOn():
    try:
        cur = conn.cursor()
        cur.execute("update user set userID=1 where userName='Temp'")
        #fetchdata = cur.fetchall()
        print("Led ON")
        cur.close()
    except Exception as e:
        print(e)
    return "Changed to 1"


@app.route('/led0')
def ledOff():
    try:
        cur = conn.cursor()
        cur.execute("update user set userID=0 where userName='Temp'")
        #fetchdata = cur.fetchall()
        print("Led OFF")
        cur.close()
    except Exception as e:
        print(e)
    return "Changed to 0"


@app.route('/getTemp')
def pint():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")
        fetchdata = cur.fetchall()
        cur.close()
    except Exception as e:
        print(e)
 # return render_template('home.html',data = fetchdata)
    return str(fetchdata)


app.run("0.0.0.0", port=8080, debug=False)
