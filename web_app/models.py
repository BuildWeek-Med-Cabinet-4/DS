from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128))
    lastName = db.Column(db.String(128))
    userName = db.Column(db.String(128))
    passWord = db.Column(db.String(128))


class Strain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    STRAIN_TYPE = db.Column(db.String(128))
    STRAIN_EFFECTS= db.Column(db.String(200))
    STRAIN_DESCRIPTION = db.Column(db.TEXT(200))
    STRAIN_FLAVORS = db.Column(db.String(200))
    