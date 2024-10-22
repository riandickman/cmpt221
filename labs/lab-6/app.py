from flask import Flask, request, render_template, redirect, url_for, session
from sqlalchemy import select
from db.server import db  
from db.schema.user import User 

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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

  
        existing_user = db.session.execute(select(User).where(User.email == email)).scalar_one_or_none()
        if existing_user:
            return redirect(url_for('signup'))  

  
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password 
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']


        user = db.session.execute(select(User).where(User.email == email)).scalar_one_or_none()

        if user and user.password == password:
            session['user_id'] = user.id
            session['email'] = user.email
            return redirect(url_for('index')) 
        else:
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/users')
def users():
    with app.app_context():

        stmt = select(User)
        all_users = db.session.execute(stmt).scalars().all()  
        return render_template('users.html', users=all_users)

if __name__ == "__main__":
    app.run(debug=True)
