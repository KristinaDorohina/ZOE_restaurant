"""Формы регистрации, отзывы, обратная связь"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.simple import EmailField, FileField
from wtforms.validators import DataRequired, email, Optional, Length, Email, EqualTo


class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Запомнить меня')
  submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = EmailField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Пароль', validators=[DataRequired()])
  confirm_password = PasswordField('Подтвердите пароль', validators=[EqualTo('password')])
  phone = StringField('Телефон', validators=[Optional()])
  avatar = FileField('Изображение профиля', validators=[Optional(), FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
  discount_card = StringField('Номер дисконтной карты', validators=[Optional(), Length(min=6, max=15)])
  submit = SubmitField('Регистрация')