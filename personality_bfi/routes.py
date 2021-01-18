# from personality_bfi import app

import pandas as pd


@app.route("/")
@app.route("/index/")
def index():
    return "home page"


@app.route("/bfi/")
def bfi():
    df_questionnaire = pd.read_csv(
        "personality_bfi/static/data/bfi-questions.csv", index_col=0
    )

    return df_questionnaire.to_html()
