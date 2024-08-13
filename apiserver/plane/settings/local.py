"""Development settings"""

import os

from .common import *  # noqa

DEBUG=0

# Debug Toolbar settings
INSTALLED_APPS += ("django.contrib.staticfiles","debug_toolbar",)  # noqa
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)  # noqa

REDIS_HOST="127.0.0.1"

REDIS_PORT="6379"
REDIS_URL="redis://127.0.0.1:6379/"
DATABASE_URL='postgresql://postgres@localhost:5433/plane_db'
REDIS_SSL = REDIS_URL and "rediss" in REDIS_URL
DEBUG_TOOLBAR_PATCH_SETTINGS = False
SECRET_KEY="60gp0byfz2dvffa45cxl20p1scy9xbpf6d8c5y0geejgkyp1b5"
# Only show emails in console don't send it to smtp
CORS_ALLOWED_ORIGINS=["http://localhost:3000", "https://localhost:3000", "http://0.0.0.0:3000"]
CSRF_TRUSTED_ORIGINS=["http://localhost:3000", "https://localhost:3000", "http://0.0.0.0:3000"]
EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend"
)
CSRF_COOKIE_SECURE=False

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,  # noqa
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        }
    }

INTERNAL_IPS = ("127.0.0.1",)

MEDIA_URL = "/uploapds/"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")  # noqa

LOG_DIR = os.path.join(BASE_DIR, "logs")  # noqa

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "plane": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
