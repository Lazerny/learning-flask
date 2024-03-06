from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField("Продолжительность")
    coloborators = StringField("Команда", validators=[DataRequired()])
    is_finished = BooleanField("Выполнено")
    submit = SubmitField('Добавить')