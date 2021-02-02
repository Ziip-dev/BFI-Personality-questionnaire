"""WTForm questionnaire file"""

from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class BfiQuestionnaire(FlaskForm):
    answer = RadioField(
        choices=[
            (1, "désapprouve fortement"),
            (2, "désapprouve un peu"),
            (3, "n'approuve ni ne désapprouve"),
            (4, "approuve un peu"),
            (5, "approuve fortement"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Question Suivante")
