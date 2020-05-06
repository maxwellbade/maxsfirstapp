import os
from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
db = SQLAlchemy(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["DATABASE_URL"] = "postgres://rwrcnqrhxbivcq:2adce3ab6fe7392c7dc3b5543d3fcee58d39ecace297d53836a217d2497b1e31@ec2-3-91-139-25.compute-1.amazonaws.com:5432/d4f4ksem4rlsv2"
Session(app)

@app.route("/")
def registration():
    return render_template("registration.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/add/')
def webhook():
    name = "ram"
    email = "ram@ram.com"
    u = User(id = id, nickname = name, email = email)
    print("user created", u)
    db.session.add(u)
    db.session.commit()
    return "user created"

@app.route('/delete/')
def delete():
    u = User.query.get(i)
    db.session.delete(u)
    db.session.commit()
    return "user deleted"

if __name__ == '__main__':
    app.run()
