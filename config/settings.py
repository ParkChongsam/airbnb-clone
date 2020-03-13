"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "z4c%$hh_-753)vt_5118gznytayq8bv#z_uu9-nnp6ic+b3(in"

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = ["django_countries", "django_seed"]
# https://github.com/Brobin/django-seed

PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig",
    "reviews.apps.ReviewsConfig",
    "reservations.apps.ReservationsConfig",
    "lists.apps.ListsConfig",
    "conversations.apps.ConversationsConfig",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

AUTH_USER_MODEL = "users.User"

MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
# #사진들이 저장될 uploads폴더가 생성됨

MEDIA_URL = "/media/"

# 실제 보여질 url(media)를 정의함.
# MEDIA_URL = "/media/"에서 처럼 media/앞에 /를 써주면 절대경로로 바뀐다
# http://127.0.0.1:8000/admin/rooms/photo/4/change/media/room_photos/nod.png
# 이처럼 못생겼던 경로가 절대경로로 바뀐다. 앞쪽에 / 하나를 써줌으로써
# 그래서 경로가 루트 디렉토리 다음으로 써진다 http://127.0.0.1:8000/media/room_photos/nod.png

# Email Configuration - mailgun의  내 계정 stting값 넣어주기

EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "airbnb@sandboxc1dde94e10884329b4ef5086ce738045.mailgun.org "
EMAIL_HOST_PASSWORD = "5b8e2b3cf435ba00cfcfbf30487cb077-ee13fadb-48d6e96d"
