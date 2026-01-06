from .base import *
import os

# --------------------------------------------------
# PRODUCTION SETTINGS
# --------------------------------------------------

DEBUG = False

# --------------------------------------------------
# ALLOWED HOSTS
# --------------------------------------------------

# Example: ALLOWED_HOSTS=clinicsetu.com,www.clinicsetu.com
ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("ALLOWED_HOSTS", "").split(",")
    if host.strip()
]

# --------------------------------------------------
# DATABASE (PostgreSQL)
# --------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

# --------------------------------------------------
# SECURITY SETTINGS
# --------------------------------------------------

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Django 4.2+ requirement for HTTPS
CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in ALLOWED_HOSTS
]

# --------------------------------------------------
# STATIC FILES (WhiteNoise)
# --------------------------------------------------

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# Enable WhiteNoise middleware
MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.security.SecurityMiddleware") + 1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)
