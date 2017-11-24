from flask import Flask, render_template, json, request
#from flask.ext.mysql import flask_mysql
from flaskext.mysql import MySQL
#from flask_mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

# app = Flask(__name__)
# @app.route("/")
# def main():
#     return render_template('index.html')
# if __name__ == "__main__": # check if the executed file is the main program and run the app
# 	app.run()

# @app.route('/showSignUp') # render the signup page once a request comes to /showSignUp
# def showSignUp():
# 	return render_template('signup.html')


app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'bunmaster'
app.config['MYSQL_DATABASE_PASSWORD'] = 'michelle'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def main():
	return render_template('index.html')
	
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    # create user code will be here; read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})



if __name__ == "__main__": # check if the executed file is the main program and run the app
	app.run()
