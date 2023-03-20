from flask_wtf import FlaskForm
from wtforms.fields import HiddenField, StringField, IntegerField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo , Length

class LoginForm(FlaskForm):
    next = HiddenField() # used to track the last page the user was in before logging out   
    email = EmailField('Email',validators=[DataRequired(),Email("Please Enter a right Email form")])
    password = PasswordField('Password',validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Usernmae',validators=[Length(max=20)])
    email = EmailField('Email',validators=[DataRequired(),Email("Please Enter a right Email form")])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4,message="Password length shouldn't be less than 4")])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo("password")])

