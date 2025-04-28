

from pathlib import Path
import os
import environ
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['192.168.0.100', '127.0.0.1','5749-103-109-53-5.in.ngrok.io']
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# ALLOWED_HOSTS = ['mobile view', 'local host','ngrok -- keeps on changing']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hospital.apps.HospitalConfig',
    'hospital_admin.apps.HospitalAdminConfig',
    'doctor.apps.DoctorConfig',
    'pharmacy.apps.PharmacyConfig',
    'sslcommerz.apps.SslcommerzConfig',
    'widget_tweaks',
    'rest_framework',
    'ChatApp.apps.ChatappConfig',
    'debug_toolbar',
 

]

MIDDLEWARE = [

   
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
     'healthstack.auto_login_middleware.AutoLoginSuperUserMiddleware',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = 'healthstack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'healthstack.wsgi.application'


DATABASES = {
    'default': {
        
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/India'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STORE_ID = env('STORE_ID')
STORE_PASSWORD = env('STORE_PASSWORD')
STORE_NAME = env('STORE_NAME')
SMTP_HOST = env('SMTP_HOST')
SMTP_PORT = env('SMTP_PORT')
SMTP_USER = env('SMTP_USER')
SMTP_PASSWORD = env('SMTP_PASSWORD')

# EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_PORT = SMTP_PORT
EMAIL_HOST_USER = SMTP_USER
EMAIL_HOST_PASSWORD = SMTP_PASSWORD
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'hospital.User'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

SESSION_COOKIE_AGE = 45*60
SESSION_SAVE_EVERY_REQUEST = True