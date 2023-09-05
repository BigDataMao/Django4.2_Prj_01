from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent


# 项目秘钥,无需修改
SECRET_KEY = "django-insecure-g2_&xa)bkl)z5pf$1ztm+%70)4m7))wktcatr#7=s)c)*h9kke"

# 开发模式True,代表调试,会自动刷新
DEBUG = True

# 允许访问的主机,'*'代表所有
ALLOWED_HOSTS = ['*']


# 定义应用
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 定义自己的应用
    "app01.apps.App01Config",
]

# 中间件
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 根路由
ROOT_URLCONF = "DjangoPrj_01.urls"

# 模板路径
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": []
        ,
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

# WSGI目录
WSGI_APPLICATION = "DjangoPrj_01.wsgi.application"


# 数据库配置
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# 数据库配置:自己的MySQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django_prj_01",
        "USER": "root",
        "PASSWORD": "mxw19910712@MYSQL",
        "HOST": "txy",
        "PORT": "3306",
    }
}


# 密码校验
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# 国际化
LANGUAGE_CODE = "en-us"  # en-us代表英文,中文为zh-hans
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# 静态文件 (CSS, JavaScript, Images)
STATIC_URL = "static/"

# 默认自动创建的主键类型
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
