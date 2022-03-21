from dataclasses import dataclass
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.create_all()

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
)

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  body = db.Column(db.String(500))
  tags = db.relationship('Tag', secondary=tags, lazy='subquery')
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@dataclass
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), nullable=False)
  posts = db.relationship('Post', backref='user', lazy=True)

  def __init__(self, email):
    self.email = email

class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)

@app.route('/create-user', methods=['POST'])
def createUser():
  email = request.json['email']
  db.session.add(User(email))
  db.session.commit()

  return jsonify(User(email))

@app.route('/users', methods=['GET'])
def getUsers():
  all_users = User.query.all()
  return jsonify(all_users)