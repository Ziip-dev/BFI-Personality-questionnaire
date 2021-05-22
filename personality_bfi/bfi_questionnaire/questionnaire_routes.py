"""BFI questionnaire routes"""

import csv
from os import getcwd, mkdir, path

from flask import Blueprint
from flask import current_app as app
from flask import g, redirect, render_template, session, url_for

from .compute_traits import calculate_user_trait_scores, fetch_question
from .questionnaire import BfiQuestionnaire, UserInfo

# Blueprint configuration
questionnaire_bp = Blueprint(
    "questionnaire_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


# Blueprint routes
@questionnaire_bp.route("/", methods=["GET"])
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
            return redirect(url_for("questionnaire_bp.bfi_end"))

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


@questionnaire_bp.route("/bfi/questionnaire/end/", methods=["GET", "POST"])
def bfi_end():
    form = UserInfo()

    # POST - retrieve user info, store it, and redirect to results page
    if form.validate_on_submit():
        # retrieve user info from the form
        email = form.email.data
        phone = form.phone.data
        age = form.birth.data
        genre = form.genre.data

        # store user info in the session cookie (client-side)
        session["user_info"] = {
            str("email"): email,
            str("phone"): phone,
            str("age"): age,
            str("genre"): genre,
        }

        # redirect to results page
        return redirect(url_for("questionnaire_bp.bfi_results"))

    # GET (render questionnaire end page with user info form)
    else:
        return render_template("end.jinja2", form=form)


@questionnaire_bp.route("/bfi/results/")
def bfi_results():
    # retrieve user answers from session cookie
    try:
        user_answers = session["user_answers"]

    except KeyError:
        return "Vous devez d'abord compléter le questionnaire, nous ne pouvons pas deviner votre personnalité ;)"

    # retrieve user info and compute trait scores
    user_info = session["user_info"]
    user_trait_scores = calculate_user_trait_scores(user_answers)

    # merge user info + user trait scores into a single dict
    user_info.update(user_trait_scores)

    # check data directory existence
    data_dir = f"{getcwd()}/personality_bfi/bfi_questionnaire/data/"
    if not path.isdir(data_dir):
        mkdir(data_dir)

    # write user info to users file with header first if file doesn't exist
    data_file = path.join(data_dir, "users.csv")

    if path.exists(data_file):
        with open(data_file, "a") as f:
            w = csv.DictWriter(f, user_info.keys())
            w.writerow(user_info)

    else:
        with open(data_file, "a") as f:
            w = csv.DictWriter(f, user_info.keys())
            w.writeheader()
            w.writerow(user_info)

    # return results page
    return render_template("results.jinja2", user_trait_scores=user_trait_scores)
