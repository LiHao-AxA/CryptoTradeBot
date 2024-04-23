#ctbot_backend/ctbot_backend/settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-=kg3m29v3!q-yvo(^+czsmey*h_mi2g_j&8-3zy14hv633$c*6'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','localhost','147.78.247.244','liuliang.life','www.liuliang.life']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
    'corsheaders',
]

MIDDLEWARE_CLASSES = [
                    'corsheaders.middleware.CorsMiddleware',
                    ]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 允许所有 IP 访问，不设置白名单
CORS_ORIGIN_ALLOW_ALL = True
# 允许携带凭证（cookies）
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
                        'http://localhost:8080',
                        'http://localhost:8000',
                        'http://liuliang.life:8080',
                        'http://liuliang.life:8000',
                        'https://liuliang.life:8080',
                        'https://liuliang.life:8000',
                        'http://www.liuliang.life:8080',
                        'http://www.liuliang.life:8000',
                        'https://www.liuliang.life:8080',
                        'https://www.liuliang.life:8000',
                        ]  # 这里将允许的前端应用的地址添加进来

# 替换成您的前端 URL
CSRF_TRUSTED_ORIGINS = [
                        'http://localhost:8080',
                        'http://localhost:8000',
                        'http://liuliang.life:8080',
                        'http://liuliang.life:8000',
                        'https://liuliang.life:8080',
                        'https://liuliang.life:8000',
                        'http://www.liuliang.life:8080',
                        'http://www.liuliang.life:8000',
                        'https://www.liuliang.life:8080',
                        'https://www.liuliang.life:8000',
                        ]
# 替换成您的前端 URL
CORS_ORIGIN_WHITELIST = [
                        'http://localhost:8080',
                        'http://localhost:8000',
                        'http://liuliang.life:8080',
                        'http://liuliang.life:8000',
                        'https://liuliang.life:8080',
                        'https://liuliang.life:8000',
                        'http://www.liuliang.life:8080',
                        'http://www.liuliang.life:8000',
                        'https://www.liuliang.life:8080',
                        'https://www.liuliang.life:8000',
                        ]

CSRF_TRUSTED_ORIGINS_HOSTS = [
                            'http://localhost:8080',
                            'http://localhost:8000',
                            'http://liuliang.life:8080',
                            'http://liuliang.life:8000',
                            'https://liuliang.life:8080',
                            'https://liuliang.life:8000',
                            'http://www.liuliang.life:8080',
                            'http://www.liuliang.life:8000',
                            'https://www.liuliang.life:8080',
                            'https://www.liuliang.life:8000',
                            ]
# 允许的请求方法
CORS_ALLOW_METHODS = (
    'DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'VIEW',
)
# 允许的请求头
CORS_ALLOW_HEADERS = (
    'accept', 'accept-encoding', 'authorization', 'content-type',
    'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with', 'X-CSRFToken'
)


ROOT_URLCONF = 'ctbot_backend.urls'

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

WSGI_APPLICATION = 'ctbot_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ctbot',
        'USER': 'root',
        'PASSWORD': 'liu627370190',
        'HOST': 'localhost',
        'PORT': '3306',
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


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGS_DIR = os.path.join(BASE_DIR, 'logs')

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, 'django.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}