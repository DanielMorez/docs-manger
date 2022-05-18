import os

from .utils import str_to_bool

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Инициализация конфига
CONFIG = __import__("app.config").config

SECRET_KEY = CONFIG.SETTINGS["SECRET_KEY"]

# На prod версии проекта ОБЯЗАТЕЛЬНО ставить False
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    # admin
    'nested_admin',
    'grappelli.dashboard',
    'grappelli',
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # other apps
    'import_export',
    'phonenumber_field',
    'rest_framework',
    'corsheaders',
    'manager'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Для избавления CORS ошибок
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

# Настройка CORS
# Более подробно тут - https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Настрока админ панели Grappelli
# Более подробно тут - https://django-grappelli.readthedocs.io/en/latest/dashboard_setup.html
GRAPPELLI_ADMIN_TITLE = "Инструмент для управления нормативно-справочной информацией"
GRAPPELLI_INDEX_DASHBOARD = "app.dashboard.Dashboard"

# Настройка базы данных
USE_SQLITE = str_to_bool(CONFIG.SETTINGS.get("USE_SQLITE", "False"))

if not USE_SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': CONFIG.SETTINGS["DB_NAME"],
            'USER': CONFIG.SETTINGS["DB_USER"],
            'PASSWORD': CONFIG.SETTINGS["DB_PASSWORD"],
            'HOST': CONFIG.SETTINGS["DB_HOST"],
            }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Для более углубленного поиска статики
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Настройки Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

# Настройка Filebrowse + получение статики/файлов из админки
DIRECTORY = ''
FILEBROWSER_DIRECTORY = ''

STATIC_URL = '/static/'
# При первой загрузке статики совершить действия, после вернуть обратно:
STATIC_ROOT = ""                                                    # <- Закомментировать
STATICFILES_DIRS = (                                                # <- Закомментировать
    CONFIG.PATHS["STATIC_DIR"],                                     # <- Закомментировать
)                                                                   # <- Закомментировать
# STATIC_ROOT = CONFIG.PATHS["STATIC_DIR"]                          # <- Раскомментировать

MEDIA_URL = '/data/'
MEDIA_ROOT = CONFIG.PATHS["DATA_DIR"]

IMPORT_EXPORT_IMPORT_PERMISSION_CODE = 'view'
IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
