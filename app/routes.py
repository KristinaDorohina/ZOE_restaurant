"""Здесь все маршруты"""

import os
from datetime import datetime

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from config import Config


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Вход выполнен успешно!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неверное имя пользователя или пароль', 'danger')
    return render_template('login.html', title='Login', form=form)



@app.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():

        try:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password_hash=generate_password_hash(form.password.data),
                phone=form.phone.data if form.phone.data else None,
                discount_card=form.discount_card.data if form.discount_card.data else None,
                is_admin=False,
                created_at=datetime.now()
            )

            if form.avatar.data:
                filename = secure_filename(form.avatar.data.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                form.avatar.data.save(filepath)
                user.avatar = filename

            db.session.add(user)
            db.session.commit()

            flash('Регистрация прошла успешно! Теперь вы можете войти.', 'success')
            return redirect(url_for('login'))

        except IntegrityError:
            db.session.rollback()
            flash('Пользователь с таким email или именем уже существует!', 'danger')
        except Exception as e:
            db.session.rollback()
            flash(f'Произошла ошибка при регистрации: {str(e)}', 'danger')

    return render_template('registration.html', title='Регистрация', form=form)
