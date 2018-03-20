from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Email 
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators = [DataRequired()])
    lastname = StringField('Last Name', validators = [DataRequired()])
    gender = SelectField(u'Gender', choices=[('Female', 'Female'), ('Male', 'Male')])
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    location = StringField('Location', validators = [DataRequired()])
    biography = TextAreaField('Biography', validators = [DataRequired()])
    photo = FileField ('Photo', validators = [FileRequired(), FileAllowed(['jpg','png'])])
   