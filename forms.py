from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,EqualTo, Email


# DataRequired == Making sure the field is filled in
# EqualTo == Making sure the field(s) are the same (I.E Passwprd and Confirm Password)
# Email == Making sure the field has a proper email given to it

class UserInfoForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    phone = StringField('Phone', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()