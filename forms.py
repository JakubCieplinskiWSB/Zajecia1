from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class IndexForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired()])
    rss = StringField('RSS', validators = [DataRequired()])
    rssList = TextAreaField('')
    save = SubmitField('Save')
    send = SubmitField('Send')