"""
Django base settings for config project.

This file contains COMMON settings shared by:
- local.py
- production.py

Do NOT put environment-specific values directly here.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------

# BASE_DIR points to the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# --------------------------------------------------
# ENVIRONMENT VARIABLES
# --------------------------------------------------

# Load variables from .env (used in local & production)
load_dotenv(BASE_DIR / ".env")

# --------------------------------------------------
# SECURITY
# --------------------------------------------------

# Secret key must always come from environment variables
SECRET_KEY = os.getenv("SECRET_KEY")

# --------------------------------------------------
# DEBUG
# --------------------------------------------------

# Always False in base (override in local.py)
DEBUG = False

# --------------------------------------------------
# ALLOWED HOSTS
# --------------------------------------------------

# Override in local.py and production.py
ALLOWED_HOSTS = []

# --------------------------------------------------
# APPLICATION DEFINITION
# --------------------------------------------------

INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# --------------------------------------------------
# PROJECT & THIRD-PARTY APPS
# --------------------------------------------------

EXTERNAL_APPS = [
    # Core apps
    'apps.accounts',
    'apps.hospitals',
    'apps.patients',
    'apps.visits',
    'apps.consultations',
    'apps.prescriptions',
    'apps.pharmacy',
    'apps.audit',
    'apps.medicines',

    # Third-party
    'rest_framework',
    'django_extensions',

    # Demo / temporary
    'apps.discovery',
]

INSTALLED_APPS += EXTERNAL_APPS

# --------------------------------------------------
# DJANGO REST FRAMEWORK
# --------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Enable in production.py if using WhiteNoise
    # 'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------------------------------
# URLS
# --------------------------------------------------

ROOT_URLCONF = 'config.urls'

# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --------------------------------------------------
# WSGI
# --------------------------------------------------

WSGI_APPLICATION = 'config.wsgi.application'

# --------------------------------------------------
# AUTHENTICATION
# --------------------------------------------------

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

# --------------------------------------------------
# DATABASE
# --------------------------------------------------

# Database must be defined in local.py / production.py
DATABASES = {}

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------
# CUSTOM USER MODEL
# --------------------------------------------------

AUTH_USER_MODEL = "accounts.User"

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------

STATIC_URL = '/static/'

# Enable in production.py
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --------------------------------------------------
# MEDIA FILES
# --------------------------------------------------

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --------------------------------------------------
# DEFAULT PRIMARY KEY FIELD
# --------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
