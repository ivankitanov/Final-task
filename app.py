from flask import Flask, request, jsonify
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from api.v1 import auth 
from models import usermodels



app = Flask(__name__)

@app.route('/')
def show_page():
    return "INF310c - Final Exam"


