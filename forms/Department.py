from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField('Название отдела', validators=[DataRequired()])
    members = StringField("Команда", validators=[DataRequired()])
    email = EmailField("Почта отдела", validators=[DataRequired()])
    submit = SubmitField('Добавить')