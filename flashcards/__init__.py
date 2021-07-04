import os
import logging.config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


BASE_DIR = os.path.dirname(__file__)

# init app:
app = Flask(__name__)

# load config:
app.config.from_pyfile(os.path.join(BASE_DIR, "config.py"))

# init db:
db = SQLAlchemy(app)

# disable warkezeug server messages:
log = logging.getLogger('werkzeug')
log.disabled = True

# init logger:
logging_conf_path = os.path.join(BASE_DIR, "logging.conf")
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger("logger_root")


from flashcards import routes
