from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=150)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password',message='Passwords must match')])
    submit = SubmitField('Register')


class ExpenseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    description = StringField('Description')
    date = StringField('Date', validators=[DataRequired()])
    note = StringField('Note')
    submit = SubmitField('Add Expense')