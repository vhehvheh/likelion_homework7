import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k)jrje5vwak-h^fs(_89-j!_d!92pr*y+yje*s5g2j)uhuokyr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',#enroll rest_framework to the installed_apps
    'post',
    'userpost',
    'rest_framework.authtoken',
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

ROOT_URLCONF = 'firstrest.urls'

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

WSGI_APPLICATION = 'firstrest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'#전역으로 설정.view의 모든 record가 default로 이렇게 pagenation

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#pagemation : record(queryset)를 정렬한 상태에서 이걸 수행해야하는 걸 추천.
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3#1 page->3 record
}
"""
REST_FRAMEWORK = {#전역으로 authentication 설정.(basic/session)
    'DEFAULT_AUTHENTICATION_CLASSES': [# 내가 사용하고 싶은 default authentication인증방식을 적어주면 됨.
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
    
}"""
#BasicAuthentication : http 자체 기본인증에 기반한 방식.
#TokenAuthentication : 사용자가 인증요청을 보내면 user별 유일한 인증 key를 제공. basic을 보안함.모바일에서 주로 사용.
#username,pw = 1:1, key(token)-> api req에 담아 처리.별도의 app(key,user field)설치, migrate해줘야함.
#remote,, : 원격지에서 사용하는 인증방식.
"""
REST_FRAMEWORK = {#DEFAULT_PERMISSION
    
}"""
#permission class 종류
#allowany(default. 걍 요청만하면 다 허용), isauthenticated(인증된 요청에만 view호출),isadminuser(staff만 허용), isauthenticatedorreadonly(비인증&안전한 http M만->readonly만 가능.)
