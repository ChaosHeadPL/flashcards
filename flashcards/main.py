import logging
from logging.config import dictConfig
from fastapi import FastAPI
from typing import Optional
from settings.logging import LogConfig

# init app:
app = FastAPI()

# init logger:
dictConfig(LogConfig().dict())
log = logging.getLogger("mycoolapp")


from .routes import *
