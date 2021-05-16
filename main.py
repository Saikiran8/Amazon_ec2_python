from flask import Flask,render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Saikiran@86'
app.config['MYSQL_DATABASE_DB'] = 'users'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
@app.route('/')
def home():
    try:
        cur = conn.cursor()
        cur.execute("select userID from user where userName='Temp';")
        fetchdata = cur.fetchall()
        cur.close()
    except Exception as e:
        print(e)
    return '{"2":"'+str(fetchdata[0][0])+'"}'
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
 #return render_template('home.html',data = fetchdata)
    return str(fetchdata)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=False)