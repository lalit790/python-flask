from flask import Flask,request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'redhat'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def hello():
    return "Welcome to Python Flask App!"

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"


if __name__ == "__main__":
    app.run()


####------you can browse the below url on browser to check ----------

###need to create a database entry like below:-

####
"""
mysql> use EmpData;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-------------------+
| Tables_in_empdata |
+-------------------+
| User              |
+-------------------+
1 row in set (0.00 sec)

mysql> select * from User;
+--------+----------+----------+
| userId | userName | password |
+--------+----------+----------+
|      1 | Admin    | admin    |
+--------+----------+----------+
1 row in set (0.00 sec)

"""
#http://127.0.0.1:5000/Authenticate?UserName=Admin&Password=admin
