from flask_sqlalchemy import SQLAlchemy 

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True)
  Email = db.Column(db.String(100), unique= True)
  password = db.Column(db.String(20) unique=True)

  def __init__(self,id, username, Email, password): 
    self.id= id
    self.username = username
    self.Email = Email
    self.password = password