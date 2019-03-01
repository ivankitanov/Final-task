from flask import Flask , request, jsonify
from flask import Blueprint
from models import usermodels
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 


auth = Blueprint('auth', __name__,template_folder='templates')

db = SQLAlchemy(auth)
user_schema = UserSchema(strict=True)
user_schema = UseerSchema(many=True, strict=True)

@auth.route('/<word>', methods=['GET'])
def get_message(word):
  if word =="Test":
      return "Yes", 200
  else:
      return "No" , 403  

@auth.route('/<word>', methods=['Post'])
def post_message(word):
    return word


@auth.route('/user<id,username,Email,password>', methods=['Post'])
def add_new_user(id,username,Email,password):
    id = request.json['id']
    username = request.json['username']
    Email = request.json['Email']
    password = request.json['password']
    new_user = User(id, username, Email, password)
    db.session.add(new_user)
    db.session.commit()

@auth.route('/user/<id>', methods=['GET'])
def get_user(id):
  user = User.query.get(id)
  return user_schema.jsonify(user)
