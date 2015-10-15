from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

#Functions
from query import confirmLogin, registerUser


app = Flask(__name__)
conn=sqlite3.connect("users.db")
c=conn.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/@<username>')
def profile(username=''):
	return render_template('profile.html')

@app.route('/@<username>/<post>')
def read():
	return render_template('post.html')

@app.route('/@<username>/<post>/comments', methods=['POST'])
def comment():
	return 'Coming Soon';

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':

        username=request.form['Username']
        password=request.form['Password']

        if confirmLogin(username,password):
            session['user']=username
            return redirect('/@'+username)
        return render_template('login.html')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':

        username=request.form['Username']
        password=request.form['Password']
        first=request.form['First Name']
        last=request.form['Last Name']

        if registerUser(first,last,username,password):
            return redirect('/new')
        return render_template('signup.html')
    return render_template('signup.html')

@app.route('/new', methods=['GET', 'POST'])
def new():
   # if request.method='POST':
   #     title=request.form['title']
   #     body=request.form['text']
   #     username=session['user']
        
        
    return render_template('new.html')

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 8000)
