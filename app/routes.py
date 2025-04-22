"""Здесь все маршруты"""
import os

from flask import render_template, flash, redirect, url_for, request
from werkzeug.security import generate_password_hash

from app import app
from app.forms import LoginForm, RegistrationForm
from config import Config


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password_hash = generate_password_hash(form.password)
        if form.avatar.data:
            avatar = form.avatar.data
            filename = Config.photos.save(form.avatar.data)
            avatar.save(os.path.join('uploads', filename))
        if form.discount_card:
            discount_card = form.discount_card
        if form.phone:
            phone = form.phone
        return redirect(url_for('login'))
    return render_template('registration.html', title='Регистрация', form=form)
