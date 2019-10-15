#!/usr/bin/env python
import sys
from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            },
        },
        INSTALLED_APPS=(
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'redis_status',
        ),
        ROOT_URLCONF='redis_status.tests.test_urls',
        SECRET_KEY='foobar',
        CACHES = {
            'default': {
                'BACKEND': 'redis_cache.RedisCache',
                'LOCATION': '%s:%s' % ('127.0.0.1', 6379),
                'OPTIONS': {
                    'DB': 0,
                    'PASSWORD': '',
                    'MIN_COMPRESSION_LEN': 102400,
                },
            }
        },
        MIDDLEWARE = [
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ],
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                    ]
                },
            },
        ]
    )


def runtests():
    argv = sys.argv[:1] + ['test'] + sys.argv[1:] + ['redis_status']
    execute_from_command_line(argv)


if __name__ == '__main__':
    runtests()