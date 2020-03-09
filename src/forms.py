from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TelecommandForm(FlaskForm):
    telecommand = StringField('telecommand', validators=[DataRequired()])
    send = SubmitField('send')
