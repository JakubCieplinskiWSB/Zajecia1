from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class IndexForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    rss = StringField('RSS')
    rssList = TextAreaField('')
    save = SubmitField('Save')
    send = SubmitField('Send')