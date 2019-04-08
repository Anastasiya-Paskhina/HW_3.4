import os
from .settings import BASE_DIR

SECRET_KEY = 'ea17k8^9x9*7^hzo7v+k8@yb)2+qtz3=17obywplqj59-_879#'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}