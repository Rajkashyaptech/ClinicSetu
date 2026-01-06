from .base import *
import os

# --------------------------------------------------
# LOCAL DEVELOPMENT SETTINGS
# --------------------------------------------------

# Enable debug mode for development
DEBUG = True

# Local secret key (recommended to load from .env)
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-local-dev-key")

# Allowed hosts for local development
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# --------------------------------------------------
# DATABASE (SQLite - Local)
# --------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
