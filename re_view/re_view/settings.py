import os
import re
from pathlib import Path

from loguru import logger

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def read_env_file_and_set_from_venv(file_name: str):
	"""Чтение переменных окружения из указанного файла, и добавление их в ПО `python`"""
	with open(file_name, 'r', encoding='utf-8') as _file:
		res = {}
		for line in _file:
			tmp = re.sub(r'^#[\s\w\d\W\t]*|[\t\s]', '', line)
			if tmp:
				k, v = tmp.split('=', 1)
				res[k] = v
	os.environ.update(res)
	print(res)


DEBUG = True

if not DEBUG:
	read_env_file_and_set_from_venv('./__env.env')

SECRET_KEY = os.environ.get("SECRET_KEY_RE_inst", "VerySecret")

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'mainapp.apps.MainappConfig',
]

MIDDLEWARE = [
		'django.middleware.security.SecurityMiddleware',
		'django.contrib.sessions.middleware.SessionMiddleware',
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.contrib.auth.middleware.AuthenticationMiddleware',
		'django.contrib.messages.middleware.MessageMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 're_view.urls'

TEMPLATES = [
		{
				'BACKEND' : 'django.template.backends.django.DjangoTemplates',
				'DIRS'    : [],
				'APP_DIRS': True,
				'OPTIONS' : {
						'context_processors': [
								'django.template.context_processors.debug',
								'django.template.context_processors.request',
								'django.contrib.auth.context_processors.auth',
								'django.contrib.messages.context_processors.messages',
						],
				},
		},
]

WSGI_APPLICATION = 're_view.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# DATABASES = {
# 		'default': {
# 				'ENGINE': 'django.db.backends.sqlite3',
# 				'NAME'  : BASE_DIR / 'db.sqlite3',
# 		}
# }


AUTH_PASSWORD_VALIDATORS = [
		{
				'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
		},
		{
				'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
		},
		{
				'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
		},
		{
				'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
		},
]

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Статические файлы
STATIC_URL = '/static/'  # URL-адрес для использования при обращении к статическим файлам, расположенным в STATIC_ROOT.
STATIC_ROOT = os.path.join(BASE_DIR, "static/")  # Путь к общей статической папки.
STATICFILES_DIRS = [  # Список нестандартных путей используемых для сборки.
		# os.path.join(BASE_DIR, "static"),
]

# Изображения
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Имя папки в корневом каталоге, для изображений
MEDIA_URL = '/media/'  # Добавляет к файлам префикс

logger.add("log/mainapp.log", level="INFO",
           format="{time:YYYY-MM-DD-HH:mm:ss}‡{message}‡{file}‡{function}‡{level}‡{line}‡{exception}‡", )

# Для отладки
# if DEBUG:
# pip install django-debug-toolbar  django-livereload-server
# INSTALLED_APPS.append('livereload')
# INSTALLED_APPS.append('debug_toolbar')
# INTERNAL_IPS = [
# 		'127.0.0.1',
# ]
# MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
# MIDDLEWARE.append('livereload.middleware.LiveReloadScript')

# Отключить кеширование при отладке
# CACHES = {
#
# 		'default': {
# 				'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
# 		}
# }
