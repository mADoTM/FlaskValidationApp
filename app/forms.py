from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    raw_data = StringField('Проверяемая строка', validators=[DataRequired()])
    regular_expression = StringField('Регулярное выражение', validators=[DataRequired()])
    submit = SubmitField('Проверить')

