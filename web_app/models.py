from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask_migrate import Migrate
from flask import jsonify

db = SQLAlchemy()
ma=Marshmallow()
migrate = Migrate()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128))
    lastName = db.Column(db.String(128))
    userName = db.Column(db.String(128))
    passWord = db.Column(db.String(128))


class Strain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strain = db.Column(db.String(128))
    effects= db.Column(db.String(200))
    description = db.Column(db.TEXT(200))
    flavor = db.Column(db.String(200))
    typeof = db.Column(db.String(200))
    #user_id = db.Column(db.Integer, db.ForeignKey(user.id))
    
    user = db.relationship('User', backref ='strain')

class UserSchema(ma.Schema):
    class Meta:
        model = User

class StrainSchema(ma.Schema):
    class Meta:
        model = Strain






    