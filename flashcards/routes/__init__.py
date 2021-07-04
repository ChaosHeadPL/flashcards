from flashcards import app

# load blueprints:
from .queue import queue


app.register_blueprint(queue)


@app.route("/", methods=["GET"])
def home():
    return "FlashCards by ChaosHead"
