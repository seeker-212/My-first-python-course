import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()

app = Flask(__name__)

# Here we set up the database configuration using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


#Main Code
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        query_stmt = (f"SELECT username FROM users WHERE username='{username}' AND password='{password}'")

        with db.engine.connect() as conn:
            result = conn.execute(text(query_stmt))
            user = result.fetchone()

        if user:
            message = f"Welcome back, {username}!"
        else:
            message = "Invalid username or password. Please try again."

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)