from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, EqualTo, Email, DataRequired
from signin.models import User

class RegisterForm(FlaskForm):
    nombre = StringField(label="Full Name", validators=[Length(min=5, max=35, message="Minimum length for name is five characters."), DataRequired(message="You must provide a name.")]) 
    username = StringField(label="Username", validators=[Length(min=3, max=10, message="Minimum length for username is three characters."), DataRequired(message="You must provide a username.")])
    email = StringField(label="Email", validators=[Email(message="Invalid email address."), DataRequired()])
    password = PasswordField(label="Password", validators=[Length(min=8, message="Minimum length for password is eight characters."), DataRequired(message="You must provide a strong password.")])
    password_confirmation = PasswordField(label="Repeat Password", validators=[EqualTo("password", message="Passwords do not match."), DataRequired()])
    submit = SubmitField(label="Sign up")

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[Email(message="Invalid email address.") ,DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")

class ResetPasswordForm(FlaskForm):
    email = StringField(label="Email", validators=[Email(message="Invalid email address.") ,DataRequired()])
    submit = SubmitField(label="Send Login Link")