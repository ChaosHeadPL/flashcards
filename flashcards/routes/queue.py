from flask import Blueprint


queue = Blueprint("queue", __name__, url_prefix="/queue")


@queue.route("/show")
def show():
    return "queue"
