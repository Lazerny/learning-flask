from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astr = IntegerField('id астронавта', validators=[DataRequired()])
    password = PasswordField('пароль астронавта', validators=[DataRequired()])
    id_cap = IntegerField('id капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')