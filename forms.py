from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class Add(FlaskForm):
    id = IntegerField('id',validators=[(DataRequired())])
    name = StringField('name', validators=[(DataRequired())])
    email = StringField('email',validators=[(DataRequired() )])
    department = StringField('department',validators=[(DataRequired() )])
    submit = SubmitField('submit',validators=[(DataRequired() )])