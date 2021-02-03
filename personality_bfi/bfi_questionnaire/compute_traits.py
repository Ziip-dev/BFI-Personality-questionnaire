import pandas as pd

# Dictionnaire des questions de chaque trait de personnalité
trait_questions = {
    "extraversion": ["1", "6R", "11", "16", "21R", "26", "31R", "36"],
    "agreabilite": ["2R", "7", "12R", "17", "22", "27R", "32", "37R", "42", "45R"],
    "conscience": ["3", "8R", "13", "18R", "23R", "28", "33", "38", "43R"],
    "nevrosisme": ["4", "9R", "14", "19", "24R", "29", "34R", "39"],
    "ouverture": ["5", "10", "15", "20", "25", "30", "35R", "40", "41R", "44"],
}


# Récupération des scores correspondant aux traits de personnalité. ATTENTION R = REVERSE (1 <--> 5 et 2 <--> 4)
def compute_trait_scores(questionnaire_df):

    # création du dictionnaire des scores
    trait_scores = {
        "extraversion": [],
        "agreabilite": [],
        "conscience": [],
        "nevrosisme": [],
        "ouverture": [],
    }

    for trait in trait_questions.keys():
        for question in trait_questions[trait]:

            # extract number only and convert to int
            question_number = int("".join(s for s in question if s.isdigit()))

            # retrieve question score and reverse if R
            if "R" in question:
                question_score = 6 - int(
                    questionnaire_df.loc[question_number]["Results"]
                )
            else:
                question_score = int(questionnaire_df.loc[question_number]["Results"])

            # storing trait scores in a dict
            trait_scores[trait].append(question_score)

    # création du dataframe trait_scores_df et alimentation (moyenne des scores de chaque trait)
    trait_scores_df = pd.DataFrame(
        data={}, columns=trait_scores.keys(), index=["score"]
    )
    for trait in trait_scores_df.columns:
        trait_scores_df[trait]["score"] = sum(trait_scores[trait]) / len(
            trait_scores[trait]
        )

    return trait_scores_df
