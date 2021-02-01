"""BFI questionnaire routes"""

from flask import Blueprint, render_template, redirect, request, url_for
from flask import current_app as app
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
        + "<a href={{ url_for('questionnaire_bp.bfi_questionnaire') }}>C'est parti !"
    )


@questionnaire_bp.route(
    "/bfi/questionnaire/<int:question_number>/", methods=["GET", "POST"]
)
def bfi_questionnaire(question_number):

    # GET (new question)
    if request.method == "GET":
        df_questionnaire = pd.read_csv(
            "personality_bfi/bfi_questionnaire/static/data/bfi-questions.csv",
            index_col=0,
        )

        try:
            question = df_questionnaire.Questions[question_number]
            return render_template(
                "questionnaire.jinja2",
                title="Big Five Inventory questionnaire",
                question_number=question_number,
                question=question,
            )

        except KeyError:
            # 404
            # return redirect("/bfi/questionnaire/<question_number/")
            return "<br> Cette question n'existe pas..."

    # POST (retrieve answer and redirect to next quetion) !
    elif request.method == "POST":
        # retrieve user answer
        answer = request.form["answer"]
        print("User answer is " + answer)
        # ImmutableMultiDict([("answer", "3"), ("next", "")])
        print("This was question " + str(question_number))

        # store it to compute scores later

        if question_number is not 45:
            question_number += 1
            # return redirect(questionnaire_bp.bfi_questionnaire)
            return redirect(
                url_for(
                    "questionnaire_bp.bfi_questionnaire",
                    question_number=question_number,
                )
            )
        else:
            return "Fin du questionnaire, merci :)"
