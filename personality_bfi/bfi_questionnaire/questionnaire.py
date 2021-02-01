"""WTForm questionnaire file"""

from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class BfiQuestionnaire(FlaskForm):
    answer = RadioField(
        "Label", choices=[("val1", "desc1"), ("val2", "desc2"), ("val3", "desc3")]
    )
    submit = SubmitField("Question Suivante")


# 1 - désapprouve fortement
# 2 - désapprouve un peu
# 3 - n'approuve ni ne désapprouve
# 4 - approuve un peu
# 5 - approuve fortement
