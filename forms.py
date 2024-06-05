from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SubmitField
from wtforms.validators import DataRequired

class AttendanceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    department = StringField('Department and Section', validators=[DataRequired()])
    purpose = StringField('Purpose of Using the Workspace', validators=[DataRequired()])
    entry_time = TimeField('Time of Entry', validators=[DataRequired()])
    exit_time = TimeField('Time of Exit', validators=[DataRequired()])
    submit = SubmitField('Submit')
