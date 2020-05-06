from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String, nullable=False)
    last = db.Column(db.String, nullable=False)
    #origin = db.Column(db.String, nullable=False)
    #destination = db.Column(db.String, nullable=False)
    #duration = db.Column(db.Integer, nullable=False)

#class Passenger(db.Model):
#    __tablename__ = "passengers"
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String, nullable=False)
#    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
