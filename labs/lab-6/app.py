from flask import Flask, request, render_template, redirect, url_for, session
from sqlalchemy import select
from db.server import db  
from db.schema.user import User 
from flask import request, render_template, redirect, url_for
from sqlalchemy import insert, text, select

from db.server import app
from db.server import db

from db.schema.user import User

from socketserver import *

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key' 


db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user_error_msg = ""
    if request.method == 'POST':
        if "email" in request.form and "password" in request.form:
            user = db.session.execute(select(User).where(User.email == request.form['email'])).scalar_one_or_none()
            if user and user.password == request.form['password']:
                session['user_id'] = user.id
                session['email'] = user.email
                return redirect(url_for('index'))
            else:
                user_error_msg = "Invalid credentials :("

    return render_template('login.html', error=user_error_msg)


@app.route('/users')
def users():
    all_users = db.session.execute(select(User)).scalars().all()
    

    return render_template('users.html', users=all_users)


@app.route('/signup', methods=['GET','POST'])
def signup():
    print(request.method)
    if request.method == 'POST':
       
        for key, value in request.form.items():
             print(f'{key}: {value}')
        query = insert(User).values(request.form)

        with app.app_context():
                db.session.execute(query)
                db.session.commit()

        return redirect (url_for ("loginpage"))


    return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    user_error_msg = ""
    if request.method == 'POST':

        if "Email" in request.form and "Password" in request.form:
        
            stmt = select(User.Password).where(User.Email == request.form['Email'])
            user = db.session.execute(stmt).fetchone()
            print(user)
            print(request.form['Password'])

            if user[0] == request.form['Password']:
                return redirect(url_for('home'))
        
            else: 
                user_error_msg = "invalid credentials :("
                return render_template('loginpage.html', error = user_error_msg)
             
    return render_template('loginpage.html', error = user_error_msg)

if __name__ == '__main__':
    app.run(debug=True)

