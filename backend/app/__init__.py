from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://taskuser:taskpassword@database:5432/taskdb'
app.config['JWT_SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)
jwt = JWTManager(app)
from app import routes