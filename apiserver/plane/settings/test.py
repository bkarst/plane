"""Test Settings"""

from .common import *  # noqa

DEBUG = True

# Send it in a dummy outbox
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

INSTALLED_APPS.append(  # noqa
    "plane.tests",
)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': ':memory:',  # Use in-memory database for tests
#         ma
#     }
# }

REDIS_HOST="127.0.0.1"

REDIS_PORT="6379"
REDIS_URL="redis://${REDIS_HOST}:6379/"
