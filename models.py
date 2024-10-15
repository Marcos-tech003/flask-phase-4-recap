from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Association table for user and group many-to-many relationship
user_groups = db.Table(
    'user_groups',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'  # Fixed tablename attribute
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    posts = db.relationship('Post', back_populates='user')
    groups = db.relationship('Group', secondary=user_groups, back_populates='users')

    @validates('username')
    def validate_username(self, key, username):
        if not (3 <= len(username) <= 20):
            raise ValueError("Username must be between 3 and 20 characters.")
        return username

class Post(db.Model):
    __tablename__ = 'posts'  # Fixed tablename attribute
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80))
    title = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='posts')

class Group(db.Model):
    __tablename__ = 'groups'  # Fixed tablename attribute
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    users = db.relationship('User', secondary=user_groups, back_populates='groups')
