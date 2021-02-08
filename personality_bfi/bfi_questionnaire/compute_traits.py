"""Module to compute user's peronality traits: it contains the function that fetch the right question to ask to the user as well as the function that calculates the user's scores from the answers dict"""


def fetch_question(question_number):
    """
    This functions holds the BFI questions.
    It takes a question number from 1 to 45 in input and returns the corresponding question.
        fetch_question(10)
        returns "s'intéresse à de nombreux sujets"
    """

    questions_dict = {
        1: "est bavard",
        2: "a tendance à critiquer les autres",
        3: "travaille consciencieusement",
        4: "est déprimé, cafardeux",
        5: "est créatif, plein d'idées originales",
        6: "est réservé",
        7: "est serviable et n'est pas égoïste avec les autres",
        8: "peut être parfois négligent",
        9: "est " "relaxe" ", détendu, gère bien les stress",
        10: "s'intéresse à de nombreux sujets",
        11: "est plein d'énergie",
        12: "commence facilement à se disputer avec les autres",
        13: "est fiable dans son travail",
        14: "peut être angoissé",
        15: "est ingénieux, une grosse tête",
        16: "communique beaucoup d'enthousiasme",
        17: "est indulgent de nature",
        18: "a tendance à être désorganisé",
        19: "se tourmente beaucoup",
        20: "a une grande imagination",
        21: "a tendance à être silencieux",
        22: "fait généralement confiance aux autres",
        23: "a tendance à être paresseux",
        24: "est quelqu'un de tempéré, pas facilement troublé",
        25: "est inventif",
        26: "a une forte personnalité, s'exprime avec assurance",
        27: "est parfois dédaigneux, méprisant",
        28: "persévère jusqu'à ce que sa tâche soit finie",
        29: "peut être lunatique d'humeur changeante",
        30: "apprécie les activités artistiques et esthétiques",
        31: "est quelque fois timide, inhibé",
        32: "est prévenant et gentil avec presque tout le monde",
        33: "est efficace dans son travail",
        34: "reste calme dans les situations angoissantes",
        35: "préfère un travail simple et routinier",
        36: "est sociable, extraverti",
        37: "est parfois impoli avec les autres",
        38: "fait des projets et les poursuit",
        39: "est facilement anxieux",
        40: "aime réfléchir et jouer avec des idées",
        41: "est peu intéressé par tout ce qui est artistique",
        42: "aime coopérer avec les autres",
        43: "est facilement distrait",
        44: "a de bonnes connaissances en art, musique ou en littérature",
        45: "cherche des histoires aux autres",
    }

    return questions_dict[question_number]


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
        user_trait_scores[trait] = round(
            sum(user_trait_scores[trait]) / len(user_trait_scores[trait]), 1
        )

    return user_trait_scores
