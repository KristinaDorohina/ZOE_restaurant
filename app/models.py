"""Здесь все модели Базы данных"""
from datetime import datetime

from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    #name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(255), nullable=True)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    discount_card = db.Column(db.String(20), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

@login.user_loader
def load_user(id):
  return db.session.get(User, int(id))