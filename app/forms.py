from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    word = StringField('Word:', validators=[InputRequired(),
    Length(min=1, max=30, message="Please enter a word between 1 and 30 characters in length")]) #{render_kw={"placeholder":"Please enter a word"}  )
    submit = SubmitField("Generate rhymes")
