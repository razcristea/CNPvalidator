from wtforms import Form, StringField, validators #run pip install WTForms in venv
from application.validators import validate_CNP


class CNPForm(Form):
    """docstring for CNP."""
    cnp_string = StringField('CNP',[validators.DataRequired(), validate_CNP])
