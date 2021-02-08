"""BFI questionnaire routes"""

from flask import Blueprint, render_template, redirect, request, url_for, session, g
from flask import current_app as app
from .questionnaire import BfiQuestionnaire
from .compute_traits import fetch_question, calculate_user_trait_scores
import pandas as pd


# Blueprint configuration
questionnaire_bp = Blueprint(
    "questionnaire_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


# Blueprint routes
@questionnaire_bp.route("/bfi/", methods=["GET"])
def bfi_welcome():
    return render_template("instructions.jinja2")


@questionnaire_bp.route(
    "/bfi/questionnaire/<int:question_number>/", methods=["GET", "POST"]
)
def bfi_questionnaire(question_number):
    form = BfiQuestionnaire()
    question_max = 45

    # POST - retrieve answer, store it, and redirect to next quetion
    if form.validate_on_submit():
        # retrieve user answer from the form
        user_answer = form.answer.data

        # store user's answer in the dict session cookie (client-side)
        if "user_answers" in session:
            session["user_answers"][str(question_number)] = user_answer
            session.modified = True
        else:
            session["user_answers"] = {str(question_number): user_answer}

        # next question
        if question_number != question_max:
            question_number += 1
            return redirect(
                url_for(
                    "questionnaire_bp.bfi_questionnaire",
                    question_number=question_number,
                )
            )
        else:
            return redirect(url_for("questionnaire_bp.bfi_results"))

    # GET (render new question)
    else:
        if 1 <= question_number <= question_max:
            g.progress = int(100 * question_number / question_max)
            question = fetch_question(question_number)
            return render_template(
                "questionnaire.jinja2",
                question_number=question_number,
                question=question,
                form=form,
            )
        else:
            return "wrong question number"


@questionnaire_bp.route("/bfi/results/")
def bfi_results():
    # retrieve user answers dict from session cookie
    try:
        user_answers = session["user_answers"]
    except KeyError:
        return "Vous devez d'abord compléter le questionnaire, nous ne pouvons pas deviner votre personnalité ;)"

    # compute score
    user_trait_scores = calculate_user_trait_scores(user_answers)

    # return results page
    return render_template("results.jinja2", user_trait_scores=user_trait_scores)
