import pandas as pd


@app.route("/bfi/")
def bfi():
    df_questionnaire = pd.read_csv(
        "personality_bfi/bfi_form/static/data/bfi-questions.csv", index_col=0
    )

    return df_questionnaire.to_html()
