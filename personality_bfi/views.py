from personality_bfi import app


@app.route("/")
def index():
    return "Hello World!"
