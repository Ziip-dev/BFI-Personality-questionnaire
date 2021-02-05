"""Module to compute user's peronality trait scores from the answers dict"""


def calculate_user_trait_scores(user_answers):
    """
    This function calculates the user's score per personality trait based on his/her 45 answers dict.
        takes in user_answers = {'1':'3', '2':'3', '2':'3', ...}
        return user_trait_scores = {
                   "extraversion": [3, 3, ...],
                   "agreabilite": [3, 3, ...],
                   "conscience": [3, 3, ...],
                   "nevrosisme": [3, 3, ...],
                   "ouverture": [3, 3, ...]
               }
    """

    # set up trait's questions
    trait_questions = {
        "extraversion": ["1", "6R", "11", "16", "21R", "26", "31R", "36"],
        "agreabilite": ["2R", "7", "12R", "17", "22", "27R", "32", "37R", "42", "45R"],
        "conscience": ["3", "8R", "13", "18R", "23R", "28", "33", "38", "43R"],
        "nevrosisme": ["4", "9R", "14", "19", "24R", "29", "34R", "39"],
        "ouverture": ["5", "10", "15", "20", "25", "30", "35R", "40", "41R", "44"],
    }

    # user traits score initialization
    user_trait_scores = {
        "extraversion": [],
        "agreabilite": [],
        "conscience": [],
        "nevrosisme": [],
        "ouverture": [],
    }

    # iterate on questions per trait
    for trait in trait_questions.keys():
        for question in trait_questions[trait]:

            # extract question number only
            question_number = "".join(s for s in question if s.isdigit())

            # retrieve user's question score and reverse if R
            if "R" in question:
                question_score = 6 - int(user_answers[question_number])
            else:
                question_score = int(user_answers[question_number])

            # store question scores in the user traits dict
            user_trait_scores[trait].append(question_score)

    # calculate the mean score per trait
    for trait in user_trait_scores:
        user_trait_scores[trait] = sum(user_trait_scores[trait]) / len(
            user_trait_scores[trait]
        )

    return user_trait_scores
