import os

# Standard-Konfiguration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "your-key-here")

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
