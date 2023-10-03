===================================================
Big Five Personality Questionnaire (French version)
===================================================


This project is a comprehensive implementation of the Big Five Inventory (BFI) personality questionnaire (French version) in a minimal Flask web app.
The BFI is a widely used psychological instrument that measures personality traits based on the Five-Factor Model (see `Big Five personality traits <https://en.wikipedia.org/wiki/Big_Five_personality_traits>`_).

According to the FFM, the five personality traits are:

- **openness to experience** (inventive/curious vs. consistent/cautious)

- **conscientiousness** (efficient/organized vs. easy-going/careless)

- **extroversion** (outgoing/energetic vs. solitary/reserved)

- **agreeableness** (friendly/compassionate vs. challenging/detached)

- **neuroticism** (sensitive/nervous vs. secure/confident)


Getting Started
===============

The app is containerised for easier testing and deployment.
You can either run it in a Docker container, automatically deploy it using Caprover on a server, or run it natively:


Docker
------

1. Run the helper script to automatically build the image and execute the container:

   ::
   
       $ ./start_container.sh


Caprover PaaS
-------------

1. Use the Caprover CLI to deploy the Dockerfile on a server and automatically build it there (your remote server has to run Caprover):

   ::
   
       $ caprover deploy


Native
------

1. Clone the repository:

   ::
   
       $ git clone https://github.com/Ziip-dev/BFI-Personality-questionnaire

2. Install the required dependencies (poetry is recommended):

   ::
   
       $ poetry install --no-dev

3. Run the Flask web server from the virtual environment:

   ::
   
       $ poetry run flask run


Software stack details
======================

I decided to keep minimal overhead with as few dependencies as possible for this little project (and to avoid javascript at all cost ;)).
The web app resolves only around Flask and Flask-WTF to create the form.
It stores answers client-side in a session cookie (dict like) and retrieve that cookie for the final calculation of the results.
The trait scores as well as user info (can remain empty for anonymity) are recorded in a csv file in the app directory.
