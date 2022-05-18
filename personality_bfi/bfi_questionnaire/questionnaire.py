"""WTForm questionnaire file"""

from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, StringField, SubmitField
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
    submit = SubmitField("Question suivante")


class UserInfo(FlaskForm):
    email    = StringField("Adresse email")
    phone    = StringField("Numéro de téléphone")
    phone_os = RadioField("Type de téléphone", choices=[("android", "android"), ("ios", "iphone")])
    birth    = IntegerField("Age")
    genre    = RadioField(choices=[("homme", "homme"), ("femme", "femme")])
    submit   = SubmitField("Terminer")
