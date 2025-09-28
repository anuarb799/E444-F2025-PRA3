import os
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

basedir = Path(__file__).resolve().parent

DATABASE = "flaskr.db"
url = os.getenv("DATABASE_URL", f"sqlite:///{Path(basedir).joinpath(DATABASE)}")

if url.startswith("postgres://"):
    url = url.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = url
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()
