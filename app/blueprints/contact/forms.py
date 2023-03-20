from flask_wtf import FlaskForm 
from wtforms.fields import TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, Email


class EmailForm(FlaskForm):
    email = EmailField("Email",validators=[DataRequired(),Email("Please Enter a Correct Email")])
    message = TextAreaField("What is your question or issue",validators=[DataRequired(),Length(1,9000)])
    