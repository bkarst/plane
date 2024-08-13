import redis
import os
from django.conf import settings
from urllib.parse import urlparse


def redis_instance():
    # connect to redis
    print('settings.REDIS_SSL')
    print(settings)
    print(settings.REDIS_SSL)
    print(settings.REDIS_URL)
    if settings.REDIS_SSL:
        print('settings.REDIS_URL')
        url = urlparse(settings.REDIS_URL)
        ri = redis.Redis(
            host=url.hostname,
            port=url.port,
            password=url.password,
            ssl=True,
            ssl_cert_reqs=None,
        )
    else:
        print("Hello")
        print(settings)
        print(os.environ.get("DATABASE_URL"))
        print(settings.DATABASE_URL)
        print(settings.REDIS_URL)
        print(settings.CELERY_BROKER_URL)
        
        ri = redis.Redis.from_url(settings.REDIS_URL, db=0)
        print("redis success")
    return ri
