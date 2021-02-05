"""BFI questionnaire routes"""

from flask import Blueprint, render_template, redirect, request, url_for, session
from flask import current_app as app
from .questionnaire import BfiQuestionnaire
from .compute_traits import calculate_user_trait_scores
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
    title = """
    Big Five Inventory Français
    """
    explanation = """
    The Big five Inventory is a personality questionnaire that relies on trait theory.
    """

    return """
    <h1>{title}</h1>
    {explanation}
    <br>
    <br>
    <a href={{ request.path }}instructions>Click here to take the test!</a>
    """.format(
        title=title, explanation=explanation
    )


@questionnaire_bp.route("/bfi/instructions/")
def bfi_instructions():
    instructions = """
    Vous allez trouver un certain nombre de qualificatifs qui peuvent ou non s'appliquer à vous.<br>
    Par exemple, acceptez-vous d'être quelqu'un qui aime passer du temps avec les autres ?<br>
    Ecrivez le chiffre indiquant combien vous approuvez ou désapprouvez l'affirmation :
    """

    # reponses_possibles
    answers_allowed = """
    1 - désapprouve fortement<br>
    2 - désapprouve un peu<br>
    3 - n'approuve ni ne désapprouve<br>
    4 - approuve un peu<br>
    5 - approuve fortement<br>
    """

    return (
        instructions
        + "<br><br>"
        + answers_allowed
        + "<br><br>"
        + "<a href={{ url_for('questionnaire_bp.bfi_questionnaire', question_number=1) }}>C'est parti !"
    )


@questionnaire_bp.route(
    "/bfi/questionnaire/<int:question_number>/", methods=["GET", "POST"]
)
def bfi_questionnaire(question_number):
    form = BfiQuestionnaire()

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
        if question_number != 45:
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
        # change to avoid reading csv file every time?
        df_questionnaire = pd.read_csv(
            "personality_bfi/bfi_questionnaire/static/data/bfi-questions.csv",
            index_col=0,
        )

        try:
            question = df_questionnaire.Questions[question_number]
            return render_template(
                "questionnaire.jinja2",
                question_number=question_number,
                question=question,
                form=form,
            )

        except KeyError:
            # return redirect("/bfi/questionnaire/<question_number/") ?
            return "<br> Cette question n'existe pas..."


@questionnaire_bp.route("/bfi/results/")
def bfi_results():
    # retrieve user answers dict from session cookie
    user_answers = session["user_answers"]

    # compute score
    user_trait_scores = calculate_user_trait_scores(user_answers)

    # return results page
    return render_template("results.jinja2", user_trait_scores=user_trait_scores)
