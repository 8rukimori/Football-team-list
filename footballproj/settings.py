from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^gax66*388v@k$*jls#w27*j+%12o5&)rgu2vn+&s0vyb^+t8f"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "footballapp.apps.FootballappConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "footballproj.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "footballproj.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = "static/"

STATICFILES_DIRS = [str(BASE_DIR / "static")]

MEDIA_ROOT = BASE_DIR / 'media/'

MEDIA_URL = 'medi/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



#Prefecture list(Value,Label)
PREFECTURES = [ 
    ("Hokkaido"  ,"Hokkaido"  ),  
    ("Aomori"  ,"Aomori"  ),  
    ("Iwate"  ,"Iwate"  ),  
    ("Miyagi"  ,"Miyagi"  ),  
    ("Akita"  ,"Akita"  ),  
    ("Yamagata"  ,"Yamagata"  ),  
    ("Fukushima"  ,"Fukushima"  ),  
    ("Ibaraki"  ,"Ibaraki"  ),  
    ("Tochigi"  ,"Tochigi"  ),  
    ("Gunma"  ,"Gunma"  ),  
    ("Saitama"  ,"Saitama"  ),  
    ("Chiba"  ,"Chiba"  ),  
    ("Tokyo"  ,"Tokyo"  ),  
    ("Kanagawa","Kanagawa"),
    ("Nigata"  ,"Nigata"  ),  
    ("Toyama"  ,"Toyama"  ),  
    ("Ishikawa"  ,"Ishikawa"  ),  
    ("Fukui"  ,"Fukui"  ),  
    ("Yamanashi"  ,"Yamanashi"  ),  
    ("Nagano"  ,"Nagano"  ),  
    ("Gifu"  ,"Gifu"  ),  
    ("Shizuoka"  ,"Shizuoka"  ),  
    ("Aichi"  ,"Aichi"  ),  
    ("Mie"  ,"Mie"  ),  
    ("Shiga"  ,"Shiga"  ),  
    ("Kyoto"  ,"Kyoto"  ),  
    ("Osaka"  ,"Osaka"  ),  
    ("Hyogo"  ,"Hyogo"  ),  
    ("Nara"  ,"Nara"  ),  
    ("Wakayama","Wakayama"),
    ("Tottori"  ,"Tottori"  ),  
    ("Shimane"  ,"Shimane"  ),  
    ("Okayama"  ,"Okayama"  ),  
    ("Hiroshima"  ,"Hiroshima"  ),  
    ("Yamaguchi"  ,"Yamaguchi"  ),  
    ("Tokushima"  ,"Tokushima"  ),  
    ("Kagawa"  ,"Kagawa"  ),  
    ("Ehime"  ,"Ehime"  ),  
    ("Kochi"  ,"Kochi"  ),  
    ("Fukuoka"  ,"Fukuoka"  ),  
    ("Saga"  ,"Shiga"  ),  
    ("Nagasaki"  ,"Nagasaki"  ),  
    ("Kumamoto"  ,"Kumamoto"  ),  
    ("Oita"  ,"Oita"  ),  
    ("Miyazaki"  ,"Miyazaki"  ),  
    ("Kagoshima","Kagoshima"),
    ("Okinawa"  ,"Okinawa"  ),  
]