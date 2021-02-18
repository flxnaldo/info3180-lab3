from flask_wtf import FlaskForm
from flask import Flask
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    subject = StringField("subject", validators=[DataRequired()])
    message = TextAreaField("message", validators = [DataRequired()])
