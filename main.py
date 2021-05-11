from flask import Flask,render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Flaks_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
@app.route('/')
def home():
    return "Hey "
@app.route('/saiki')
def pint():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM flask")
        fetchdata = cur.fetchall()
        cur.close()
    except Exception as e:
        print(e)
 #return render_template('home.html',data = fetchdata)
    return str(fetchdata)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=False)
