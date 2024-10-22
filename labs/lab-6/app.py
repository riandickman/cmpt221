from flask import Flask, request, render_template, redirect, url_for, session
from sqlalchemy import select
from db.server import db  # Assuming db is defined in server.py
from db.schema.user import User  # Import your User model

# Create a Flask application instance
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Update this to your database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Replace with a strong random key

# Initialize the database with the app
db.init_app(app)

# Create the database tables if they don't exist
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

        # Check if the email already exists
        existing_user = db.session.execute(select(User).where(User.email == email)).scalar_one_or_none()
        if existing_user:
            return redirect(url_for('signup'))  # Redirect without a flash message

        # Create a new user and store it in the database
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password  # Ideally, hash the password before storing
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

        # Query the database for the user by email
        user = db.session.execute(select(User).where(User.email == email)).scalar_one_or_none()

        # Check if user exists and if the password matches
        if user and user.password == password:
            session['user_id'] = user.id
            session['email'] = user.email
            return redirect(url_for('index'))  # Redirect to home page
        else:
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/users')
def users():
    with app.app_context():
        # Select all users
        stmt = select(User)
        all_users = db.session.execute(stmt).scalars().all()  # This should return a list of User objects
        return render_template('users.html', users=all_users)

if __name__ == "__main__":
    app.run(debug=True)
