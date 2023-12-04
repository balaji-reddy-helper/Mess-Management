from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
 
app = Flask(__name__)

db_client = MongoClient('localhost', 27017)
db = db_client['MMS']
admin = db['Admin']
student = db['Student']

user = ""
password = ""
stud_id=""


@app.route('/index1/<name>', methods = ['POST', 'GET'])
def index1(name):
	name = name.split('@')
	return render_template("index1.html", name = name[0])

@app.route('/index3/user', methods = ['POST', 'GET'])
def index3():
	return render_template("index3.html")

@app.route('/index2/student', methods = ['POST', 'GET'])
def index2(data):
	return render_template("index2.html",data=data)

@app.route('/Search', methods = ['POST', 'GET'])
def Search():
	global stud_id
	global user

	if request.method == 'POST':
			stud_id=request.form['stud_id']
			print(stud_id)
			mess=list(admin.find({"user_id":user}))
			print(mess[3])
			data=list(student.find({"mess":mess[3]}))
			print("{}".format(data[1]))
			data1=list(student.find({"stud_id":stud_id}))
			for i in range(len(data)):
    				if(stud_id==data[i][1]):
    					return redirect(url_for('index2', data = data1))
			else:
				return redirect(url_for('index3'))
    						

@app.route('/login', methods = ['POST', 'GET'])
def login():
		global user
		global password

		if request.method == 'POST':
			user = request.form['user']
			password = request.form['password']

			val = list(admin.find({"user_id":user}))
			print(val)
			val1 = list(admin.find({"password":password}))
		if(val==val1):
			return redirect(url_for('index1', name = str(user)))
		else:
			return redirect(url_for('index3'))

@app.route('/', methods = ['POST', 'GET'])
def login_view():
		return render_template("index.html");
 
if __name__ == '__main__':
    app.run(debug = True)