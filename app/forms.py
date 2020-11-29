from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, DateField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User, Venue, Event
from wtforms.fields.html5 import DateField


class CreateNewArtist(FlaskForm):
    name = StringField('Artist Name', validators=[DataRequired()])
    hometown = StringField('Hometown')
    description = TextAreaField('Description')
    submit = SubmitField('Create New Artist')

class CreateNewVenue(FlaskForm):
    name = StringField('Venue Name', validators=[DataRequired()])
    address = StringField('Address')
    city = StringField('City')
    state = StringField('State (2 letters e.g., NY, CA)')
    submit = SubmitField('Create New Venue')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')




class CreateNewEvent(FlaskForm):
    name = StringField('Event Name:', validators=[DataRequired()])
    date = DateField('Start Time:', format='%Y-%m-%d', validators=[DataRequired()])
    venue = SelectField('Venue:', coerce=int)
    artists = SelectMultipleField('Artists')
    submit = SubmitField('Create New Event')
