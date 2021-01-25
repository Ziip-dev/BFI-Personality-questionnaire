import pandas as pd


@app.route("/bfi/")
def bfi_welcome():
    titre = """
    Big Five Inventory Français
    """
    explanation = """
    The Big five Inventory is a personality questionnaire that relies on trait theory"""

    return titre + "\n\n" + explanation


@app.route("/bfi/instructions/")
def bfi_instructions():
    instructions = """
    Vous allez trouver un certain nombre de qualificatifs qui peuvent ou non s'appliquer à vous.
    Par exemple, acceptez-vous d'être quelqu'un qui aime passer du temps avec les autres ?
    Ecrivez le chiffre indiquant combien vous approuvez ou désapprouvez l'affirmation :
    """

    # reponses_possibles
    answers_allowed = """
    1 - désapprouve fortement
    2 - désapprouve un peu
    3 - n'approuve ni ne désapprouve
    4 - approuve un peu
    5 - approuve fortement
    """

    return instructions + "\n" + answers_allowed


@app.route("/bfi/questionnaire/")
def bfi_instructions():
    df_questionnaire = pd.read_csv(
        "personality_bfi/bfi_form/static/data/bfi-questions.csv", index_col=0
    )

    return df_questionnaire.to_html()
