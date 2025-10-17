from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(message="Username is required."), Length(min=6 , max=20, message="Username must be between 6 and 20 characters.")])
    email = EmailField('Email Address', validators=[DataRequired(message="Email is required."), Email()])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required."), Length(min=5 , max=20, message="Password must be between 5 and 20 characters.")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message="Password is required."),EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

class AddproductForm(FlaskForm):
    """Addproduct Form"""
    product_name = StringField('Product Name', validators=[DataRequired(message="Product name is required."),Length(min=2, max=100, message="Product name must be between 2 and 100 characters.")])
    product_decription = StringField('Product Decription', validators=[DataRequired(message="Product Decription is required."),Length(min=2, max=100, message="Product description must be between 2 and 100 characters.")])
    stock_available = SelectField('Stock Available', choices=[('1', '1'), ('5', '5'), ('12', '12'), ('20', '20')], validators=[DataRequired(message="You must fill the above.")]) 
    submit = SubmitField('Add Product')