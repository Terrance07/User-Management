#Fist import pakages like Flask , MySQL , flask-mysqldb



from flask import Flask, render_template, url_for, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#Create a user table in mysql software and connect it with python using IDE 
#Before importing create a table in MYSQL 

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Demon07@"
app.config["MYSQL_DB"] = "terrance01_db"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)


#Creating Home page


@app.route("/")
def home():
    con = mysql.connection.cursor()
    sql = "select * from users1"
    con.execute(sql)
    res = con.fetchall()
    return render_template("home.html", datas=res)


  # Adding User Details
@app.route("/addUsers", methods=['GET','POST'])
def addUsers():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        con = mysql.connection.cursor()
        sql = "insert into users1 (NAME,CITY,AGE) values (%s,%s,%s)"
        con.execute(sql, [name, city, age])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("addUsers.html")


  #Updating Existing user
# Update user
@app.route("/editUser/<string:id>", methods=['GET', 'POST'])
def editUser(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        sql = "update users1 set NAME=%s,CITY=%s,AGE=%s where ID=%s"
        con.execute(sql, [name, city, age, id])
        mysql.connection.commit()
        con.close()
        return render_template(url_for("home"))
        con = mysql.connection.cursor()
    sql = "select * from users1 where ID=%s"
    con.execute(sql, [id])
    res = con.fetchone()
    return render_template("editUser.html", datas=res)


  #Deleting user from table
# Delete User
@app.route("/deleteUser/<string:id>", methods=['GET', 'POST'])
def deleteUser(id):
    con = mysql.connection.cursor()
    sql = "delete from users1 where ID=%s"
    con.execute(sql, [id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))


if (__name__ == '__main__'):
    app.run(debug=True)    
