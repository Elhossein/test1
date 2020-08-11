from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, Required

class ContactForm(FlaskForm):
    name = TextField('Name', validators=[Required(message='you should fill this')])
    email = TextField('Email',  validators=[Required(message='you should fill this'), Email(message=('Not a valid email address.'))])
    subject = TextField("Subject",   validators=[Required(message='you should fill this')])
    message = TextAreaField('Message',  validators=[Required(message='you should fill this'), Length(min=4, message=('Your message is too short.'))])
    submit = SubmitField("Submit")

'''
class ContactForm(FlaskForm):
    name = TextField('Name', [DataRequired()])
    email = TextField('Email', [Email(message=('Not a valid email address.')), DataRequired()])
    subject = TextField("Subject",  [DataRequired()])
    message = TextAreaField('Message', [DataRequired(), Length(min=4, message=('Your message is too short.'))])
    submit = SubmitField("Submit")
'''